# Platform Contracts — Reference v2

Registry: `blueprint.json`  
Artifact: ART-017  
Status: accepted reference contract until implemented code schemas exist

These TypeScript shapes are deliberately closed. Each adapter may receive vendor values as `unknown`, but it must parse them into these unions before core code sees them. Once implemented, source types/schemas become authoritative and this file becomes generated design documentation.

## Primitive and stable identities

```ts
type Brand<Value, Name extends string> = Value & { readonly __brand: Name };

export type AgentId = Brand<string, "AgentId">;
export type PrincipalId = Brand<string, "PrincipalId">;
export type WorldId = Brand<string, "WorldId">;
export type WorldEpoch = Brand<number, "WorldEpoch">;
export type WorldSessionId = Brand<string, "WorldSessionId">;
export type EventId = Brand<string, "EventId">;
export type ConversationId = Brand<string, "ConversationId">;
export type ModelRunId = Brand<string, "ModelRunId">;
export type UtteranceId = Brand<string, "UtteranceId">;
export type ActionId = Brand<string, "ActionId">;
export type BehaviorId = Brand<string, "BehaviorId">;
export type LeaseId = Brand<string, "LeaseId">;
export type EncounterId = Brand<string, "EncounterId">;
export type OperatorRequestId = Brand<string, "OperatorRequestId">;
export type IsoTimestamp = Brand<string, "IsoTimestamp">;

export type BlockPosition = Readonly<{ x: number; y: number; z: number }>;
export type Velocity = Readonly<{ x: number; y: number; z: number }>;
```

IDs are runtime-issued. A model/provider/adapter cannot choose or overwrite them.

## Identity and world epoch

```ts
export type MinecraftPrincipalAlias =
  | Readonly<{
      kind: "authenticated_uuid";
      minecraftUuid: string;
      usernameAtObservation: string;
      validFrom: IsoTimestamp;
      validUntil?: IsoTimestamp;
    }>
  | Readonly<{
      kind: "configured_offline_username";
      username: string;
      validFrom: IsoTimestamp;
      validUntil?: IsoTimestamp;
    }>
  | Readonly<{
      kind: "session_entity";
      worldSessionId: WorldSessionId;
      entityId: number;
      observedUsername: string;
      validFrom: IsoTimestamp;
      validUntil?: IsoTimestamp;
    }>;

export type PrincipalIdentity = Readonly<{
  principalId: PrincipalId;
  role: "authorized_player" | "operator" | "other_player";
  aliases: readonly MinecraftPrincipalAlias[];
}>;

export type WorldIdentity = Readonly<{
  worldId: WorldId;
  worldEpoch: WorldEpoch;
  environmentKind: "minecraft_paper";
  fingerprint: string;
  epochReason: "initial" | "compatible_restart" | "incompatible_reset" |
    "incompatible_replacement" | "incompatible_restore";
}>;
```

`session_entity` supports presence correlation only. It never authorizes a player by itself.

## Orthogonal runtime states

```ts
export type ConnectionState =
  | "OFFLINE"
  | "CONNECTING"
  | "SYNCING"
  | "READY"
  | "DISCONNECTED"
  | "FAULTED";

export type AvailabilityState = "ACTIVE" | "SUSPENDED" | "PAUSED";

export type ComponentHealthState = "OK" | "DEGRADED" | "UNAVAILABLE" | "FAULTED";

export type RuntimeState = Readonly<{
  agentId: AgentId;
  connection: ConnectionState;
  availability: AvailabilityState;
  worldAdapterHealth: ComponentHealthState;
  modelProviderHealth: ComponentHealthState;
  storeHealth: ComponentHealthState;
  telemetryHealth: ComponentHealthState;
  activeModelRunId?: ModelRunId;
  activeActionId?: ActionId;
  activeBehaviorId?: BehaviorId;
  stateVersion: number;
  changedAt: IsoTimestamp;
}>;
```

`ACTIVE` is valid only when connection is `READY`, the authorized principal is freshly present, operator pause is false, and store/persona prerequisites pass.

## Closed world observations

```ts
type ObservationBase = Readonly<{
  schemaVersion: 2;
  worldId: WorldId;
  worldEpoch: WorldEpoch;
  worldSessionId: WorldSessionId;
  adapterSourceId: string;
  sourceSequence?: number;
  occurredAt: IsoTimestamp;
  observedAt: IsoTimestamp;
}>;

export type WorldObservation =
  | (ObservationBase & Readonly<{
      kind: "connection_changed";
      previous: ConnectionState;
      current: ConnectionState;
      reason: "operator_start" | "joined" | "sync_complete" | "link_lost" |
        "server_closed" | "operator_shutdown" | "retry" | "configuration_fault";
    }>)
  | (ObservationBase & Readonly<{
      kind: "authorized_player_presence";
      principalId: PrincipalId;
      present: boolean;
      minecraftUuid?: string;
      username: string;
      sessionEntityId?: number;
      position?: BlockPosition;
    }>)
  | (ObservationBase & Readonly<{
      kind: "player_chat_delivered";
      principalId: PrincipalId;
      conversationId: ConversationId;
      message: string;
      addressedAgentId: AgentId;
    }>)
  | (ObservationBase & Readonly<{
      kind: "agent_position";
      agentId: AgentId;
      position: BlockPosition;
      velocity: Velocity;
      onGround: boolean;
      activePathGoal: boolean;
    }>)
  | (ObservationBase & Readonly<{
      kind: "authorized_player_position";
      principalId: PrincipalId;
      position: BlockPosition;
      velocity: Velocity;
    }>)
  | (ObservationBase & Readonly<{
      kind: "nearby_entities";
      entities: readonly NearbyEntitySnapshot[];
      omittedCount: number;
      radiusBlocks: number;
    }>)
  | (ObservationBase & Readonly<{
      kind: "pathfinder_status";
      behaviorId: BehaviorId;
      status: "path_found" | "partial" | "no_path" | "path_timeout" |
        "goal_moved" | "stuck" | "goal_cleared";
      currentPosition: BlockPosition;
      targetPrincipalId?: PrincipalId;
      targetPosition?: BlockPosition;
    }>);

export type NearbyEntitySnapshot = Readonly<{
  entityRef: string;
  category: "player" | "mob" | "item" | "other";
  principalId?: PrincipalId;
  displayType: string;
  position: BlockPosition;
  distanceBlocks: number;
}>;
```

Adapter parse entrypoint:

```ts
export interface MinecraftObservationParser {
  parse(rawVendorValue: unknown):
    | Readonly<{ kind: "accepted"; observation: WorldObservation }>
    | Readonly<{ kind: "rejected"; reason: ObservationParseFailure }>;
}

export type ObservationParseFailure =
  | "malformed"
  | "unknown_kind"
  | "wrong_world"
  | "wrong_epoch"
  | "unmapped_principal"
  | "out_of_bounds"
  | "oversized";
```

## Closed snapshot/query

```ts
export type WorldQueryRequest =
  | Readonly<{
      kind: "capture_gate_a_snapshot";
      agentId: AgentId;
      worldId: WorldId;
      worldEpoch: WorldEpoch;
      radiusBlocks: number;
      entityLimit: number;
      deadlineAt: IsoTimestamp;
    }>
  | Readonly<{
      kind: "observe_behavior_stop";
      agentId: AgentId;
      behaviorId: BehaviorId;
      worldId: WorldId;
      worldEpoch: WorldEpoch;
      deadlineAt: IsoTimestamp;
    }>;

export type AgentBodySnapshot = Readonly<{
  agentId: AgentId;
  position: BlockPosition;
  velocity: Velocity;
  onGround: boolean;
  activePathGoal: boolean;
}>;

export type AuthorizedPlayerSnapshot = Readonly<{
  principalId: PrincipalId;
  present: boolean;
  usernameAtCapture: string;
  position?: BlockPosition;
  velocity?: Velocity;
}>;

export type WorldSnapshot = Readonly<{
  kind: "gate_a_world_snapshot";
  worldId: WorldId;
  worldEpoch: WorldEpoch;
  worldSessionId: WorldSessionId;
  capturedAt: IsoTimestamp;
  expiresAt: IsoTimestamp;
  agent: AgentBodySnapshot;
  authorizedPlayer: AuthorizedPlayerSnapshot;
  nearbyEntities: readonly NearbyEntitySnapshot[];
  omittedEntityCount: number;
}>;
```

## Cognition request and model decision

```ts
export type CognitionTrigger =
  | Readonly<{
      kind: "addressed_authorized_chat";
      sourceEventId: EventId;
      principalId: PrincipalId;
      conversationId: ConversationId;
    }>
  | Readonly<{
      kind: "designated_behavior_terminal";
      sourceEventId: EventId;
      behaviorId: BehaviorId;
    }>
  | Readonly<{
      kind: "designated_restart_recall";
      sourceEventId: EventId;
      encounterId: EncounterId;
    }>;

export type SourceEventExcerpt = Readonly<{
  eventId: EventId;
  kind: DurableEvent["kind"];
  occurredAt: IsoTimestamp;
  participantIds: readonly PrincipalId[];
  faithfulTextExcerpt?: string;
  capabilityOutcome?: "completed" | "failed" | "interrupted" | "cancelled" |
    "timed_out" | "unknown";
}>;

export type CognitionRequest = Readonly<{
  kind: "gate_a_cognition_request";
  modelRunId: ModelRunId;
  agentId: AgentId;
  worldId: WorldId;
  worldEpoch: WorldEpoch;
  trigger: CognitionTrigger;
  currentObservation: WorldSnapshot;
  recentConversation: readonly SourceEventExcerpt[];
  retrievedEncounter?: Readonly<{
    encounterId: EncounterId;
    promotionReason: "explicit_remember_request" | "designated_acceptance_action";
    sourceEvents: readonly SourceEventExcerpt[];
  }>;
  persona: CompiledPersonaContext;
  allowedActionKinds: readonly ["follow_player", "stop_behavior"];
  deadlineAt: IsoTimestamp;
}>;

export type UtteranceProposal = Readonly<{
  kind: "utterance_proposal";
  text: string;
  intent: "reply" | "acknowledge_action" | "grounded_recall" | "decline";
}>;

export type FollowPlayerProposal = Readonly<{
  kind: "follow_player";
  targetPrincipalId: PrincipalId;
  desiredDistanceBlocks: 2 | 3 | 4;
}>;

export type StopBehaviorProposal = Readonly<{
  kind: "stop_behavior";
  behaviorId?: BehaviorId;
}>;

export type GateAActionProposal = FollowPlayerProposal | StopBehaviorProposal;

export type ModelDecision = Readonly<{
  kind: "model_decision";
  decisionVersion: 1;
  utterance?: UtteranceProposal;
  action?: GateAActionProposal;
}>;

export type ModelRunResult =
  | Readonly<{
      kind: "completed";
      modelRunId: ModelRunId;
      decision: ModelDecision;
      providerModel: string;
      latencyMs: number;
      inputTokens?: number;
      outputTokens?: number;
    }>
  | Readonly<{
      kind: "timed_out" | "cancelled" | "provider_unavailable" |
        "provider_rejected" | "invalid_output" | "interrupted";
      modelRunId: ModelRunId;
      reason: string;
      latencyMs: number;
    }>;

export interface ModelPort {
  decide(request: CognitionRequest, signal: AbortSignal): Promise<ModelRunResult>;
}
```

Gate A does not pass action callbacks into the provider. The decision is returned, the provider call ends, and runtime workflows proceed independently.

## Utterance workflow

```ts
export type ValidatedUtterance = Readonly<{
  kind: "validated_utterance";
  utteranceId: UtteranceId;
  agentId: AgentId;
  principalId: PrincipalId;
  conversationId: ConversationId;
  modelRunId: ModelRunId;
  sourceEventId: EventId;
  text: string;
  attemptNumber: 1;
  deadlineAt: IsoTimestamp;
}>;

export type UtteranceSubmissionResult =
  | Readonly<{
      kind: "delivered";
      utteranceId: UtteranceId;
      attemptedAt: IsoTimestamp;
      environmentReceipt?: string;
    }>
  | Readonly<{
      kind: "rejected";
      utteranceId: UtteranceId;
      attemptedAt: IsoTimestamp;
      reason: "not_connected" | "not_active" | "invalid_text" | "rate_limited";
    }>
  | Readonly<{
      kind: "unknown";
      utteranceId: UtteranceId;
      attemptedAt: IsoTimestamp;
      reason: "timeout" | "disconnect_during_submission" | "interrupted_after_submit";
    }>;

export interface UtteranceSubmissionPort {
  submitOnce(
    utterance: ValidatedUtterance,
    signal: AbortSignal,
  ): Promise<UtteranceSubmissionResult>;
}
```

`attemptNumber` has only the literal value `1` in Gate A.

## Action validation and requests

```ts
export type ActionRequest =
  | Readonly<{
      kind: "follow_player";
      actionId: ActionId;
      agentId: AgentId;
      targetPrincipalId: PrincipalId;
      desiredDistanceBlocks: 2 | 3 | 4;
      worldId: WorldId;
      worldEpoch: WorldEpoch;
      sourceEventId: EventId;
      modelRunId: ModelRunId;
      snapshotCapturedAt: IsoTimestamp;
      dispatchDeadlineAt: IsoTimestamp;
    }>
  | Readonly<{
      kind: "stop_behavior";
      actionId: ActionId;
      agentId: AgentId;
      behaviorId?: BehaviorId;
      sourceEventId: EventId;
      dispatchDeadlineAt: IsoTimestamp;
    }>;

export type ActionRejectionReason =
  | "not_active"
  | "connection_not_ready"
  | "unauthorized_principal"
  | "target_not_present"
  | "target_too_far"
  | "stale_snapshot"
  | "wrong_world_epoch"
  | "lease_conflict"
  | "deadline_expired"
  | "capability_not_allowed"
  | "malformed";

export type ActionValidationResult =
  | Readonly<{ kind: "validated"; request: ActionRequest }>
  | Readonly<{ kind: "rejected"; actionId: ActionId; reason: ActionRejectionReason }>;
```

## Behavior and priority control

```ts
export type BehaviorDispatchRequest = Readonly<{
  kind: "start_follow_player";
  actionId: ActionId;
  behaviorId: BehaviorId;
  leaseId: LeaseId;
  agentId: AgentId;
  targetPrincipalId: PrincipalId;
  desiredDistanceBlocks: 2 | 3 | 4;
  worldId: WorldId;
  worldEpoch: WorldEpoch;
  dispatchDeadlineAt: IsoTimestamp;
  behaviorTimeoutAt: IsoTimestamp;
  reevaluationIntervalMs: 1000;
}>;

export type ControlRequest =
  | Readonly<{
      kind: "stop_behavior";
      operatorRequestId: OperatorRequestId;
      agentId: AgentId;
      behaviorId?: BehaviorId;
      reason: "player_request" | "operator_request";
      deadlineAt: IsoTimestamp;
    }>
  | Readonly<{
      kind: "emergency_stop";
      operatorRequestId: OperatorRequestId;
      agentId: AgentId;
      reason: "operator" | "hazard" | "suspension" | "shutdown" |
        "connection_loss";
      deadlineAt: IsoTimestamp;
    }>;

export type ImmediateDispatchResult =
  | Readonly<{
      kind: "started";
      actionId: ActionId;
      behaviorId: BehaviorId;
      leaseId: LeaseId;
      acknowledgedAt: IsoTimestamp;
    }>
  | Readonly<{
      kind: "completed";
      actionId: ActionId;
      behaviorId?: BehaviorId;
      acknowledgedAt: IsoTimestamp;
      reason: "already_stopped";
    }>
  | Readonly<{
      kind: "rejected" | "failed" | "unknown";
      actionId: ActionId;
      behaviorId?: BehaviorId;
      reason: string;
      observedAt: IsoTimestamp;
    }>;
```

## Capability evidence and behavior events

Evidence kinds have capability-specific meanings; no generic rank function is permitted.

```ts
export type CapabilityEvidence =
  | Readonly<{
      kind: "dispatch_acknowledged";
      capability: "follow_player" | "stop_behavior" | "emergency_stop";
      observedAt: IsoTimestamp;
      adapterReceipt: string;
    }>
  | Readonly<{
      kind: "client_observed_follow_motion";
      capability: "follow_player";
      observedAt: IsoTimestamp;
      agentPosition: BlockPosition;
      targetPrincipalId: PrincipalId;
      targetPosition: BlockPosition;
      distanceBlocks: number;
      activePathGoal: boolean;
    }>
  | Readonly<{
      kind: "client_observed_stop";
      capability: "stop_behavior" | "emergency_stop";
      observedAt: IsoTimestamp;
      position: BlockPosition;
      velocity: Velocity;
      activePathGoal: false;
      observationWindowMs: number;
    }>
  | Readonly<{
      kind: "server_confirmed";
      capability: "follow_player" | "stop_behavior" | "emergency_stop";
      observedAt: IsoTimestamp;
      confirmationCode: string;
    }>
  | Readonly<{
      kind: "reconciled";
      capability: "follow_player" | "stop_behavior" | "emergency_stop";
      observedAt: IsoTimestamp;
      resolvesEventId: EventId;
      resolution: "completed" | "failed" | "interrupted" | "unknown";
    }>
  | Readonly<{
      kind: "unknown";
      capability: "follow_player" | "stop_behavior" | "emergency_stop";
      observedAt: IsoTimestamp;
      reason: "disconnected" | "timeout" | "conflicting_observations" |
        "insufficient_observation";
    }>;

export type BehaviorEvent =
  | Readonly<{
      kind: "behavior_progress";
      behaviorId: BehaviorId;
      actionId: ActionId;
      at: IsoTimestamp;
      state: "active" | "replanning";
      capabilityEvidence: readonly CapabilityEvidence[];
    }>
  | Readonly<{
      kind: "behavior_terminal";
      behaviorId: BehaviorId;
      actionId: ActionId;
      at: IsoTimestamp;
      outcome: "completed" | "failed" | "interrupted" | "cancelled" |
        "timed_out" | "unknown";
      reason: string;
      capabilityEvidence: readonly CapabilityEvidence[];
      needsInterpretation: boolean;
    }>;
```

Minimum rules:

```ts
export type GateAEvidenceRule =
  | Readonly<{
      capability: "follow_player";
      activeAccepts: readonly ["client_observed_follow_motion"];
      completedAccepts: readonly ["client_observed_follow_motion", "server_confirmed"];
    }>
  | Readonly<{
      capability: "stop_behavior" | "emergency_stop";
      completedAccepts: readonly ["client_observed_stop", "server_confirmed"];
    }>;
```

`dispatch_acknowledged` alone cannot complete either capability. These rules cannot be imported into future inventory/container/item capabilities.

## Durable events and encounter

```ts
type DurableEventBase = Readonly<{
  eventId: EventId;
  schemaVersion: 2;
  agentId: AgentId;
  worldId: WorldId;
  worldEpoch: WorldEpoch;
  worldSessionId?: WorldSessionId;
  conversationId?: ConversationId;
  causedByEventId?: EventId;
  occurredAt: IsoTimestamp;
  observedAt: IsoTimestamp;
  recordedAt: IsoTimestamp;
}>;

export type DurableEvent =
  | (DurableEventBase & Readonly<{
      kind: "player_utterance_delivered";
      principalId: PrincipalId;
      text: string;
    }>)
  | (DurableEventBase & Readonly<{
      kind: "npc_utterance_proposed";
      principalId: PrincipalId;
      modelRunId: ModelRunId;
      utteranceId: UtteranceId;
      text: string;
    }>)
  | (DurableEventBase & Readonly<{
      kind: "npc_utterance_delivery_result";
      utteranceId: UtteranceId;
      result: UtteranceSubmissionResult;
    }>)
  | (DurableEventBase & Readonly<{
      kind: "model_decision_accepted";
      modelRunId: ModelRunId;
      decision: ModelDecision;
    }>)
  | (DurableEventBase & Readonly<{
      kind: "action_validation_result";
      actionId: ActionId;
      result: ActionValidationResult;
    }>)
  | (DurableEventBase & Readonly<{
      kind: "action_dispatch_result";
      actionId: ActionId;
      result: ImmediateDispatchResult;
    }>)
  | (DurableEventBase & Readonly<{
      kind: "behavior_event";
      behaviorId: BehaviorId;
      event: BehaviorEvent;
    }>)
  | (DurableEventBase & Readonly<{
      kind: "capability_evidence_observed";
      behaviorId?: BehaviorId;
      capabilityEvidence: CapabilityEvidence;
    }>)
  | (DurableEventBase & Readonly<{
      kind: "presence_changed";
      principalId: PrincipalId;
      present: boolean;
    }>)
  | (DurableEventBase & Readonly<{
      kind: "connection_changed";
      previous: ConnectionState;
      current: ConnectionState;
      reason: string;
    }>)
  | (DurableEventBase & Readonly<{
      kind: "availability_changed";
      previous: AvailabilityState;
      current: AvailabilityState;
      reason: string;
    }>)
  | (DurableEventBase & Readonly<{
      kind: "component_health_changed";
      component: "world" | "model" | "store" | "telemetry";
      previous: ComponentHealthState;
      current: ComponentHealthState;
      reason: string;
    }>)
  | (DurableEventBase & Readonly<{
      kind: "model_run_terminal";
      modelRunId: ModelRunId;
      result: Exclude<ModelRunResult, { kind: "completed" }>;
    }>)
  | (DurableEventBase & Readonly<{
      kind: "encounter_promoted";
      encounterId: EncounterId;
      promotionReason: "explicit_remember_request" | "designated_acceptance_action";
      sourceEventIds: readonly EventId[];
    }>)
  | (DurableEventBase & Readonly<{
      kind: "shutdown_started" | "shutdown_completed" |
        "restart_reconciled" | "offline_gap_recorded";
      detail: string;
    }>);

export type EncounterRecord = Readonly<{
  encounterId: EncounterId;
  agentId: AgentId;
  participantIds: readonly PrincipalId[];
  worldId: WorldId;
  worldEpoch: WorldEpoch;
  promotionReason: "explicit_remember_request" | "designated_acceptance_action";
  sourceEventIds: readonly EventId[];
  createdAt: IsoTimestamp;
}>;
```

## Derived interpretation seam (not Gate-A authority)

```ts
export type DerivedInterpretationProposal = Readonly<{
  kind: "derived_interpretation_proposal";
  agentId: AgentId;
  interpretationKind: "belief" | "episodic_summary" | "relationship_implication";
  sourceEventIds: readonly [EventId, ...EventId[]];
  text: string;
  confidence: number;
}>;

export type DerivedInterpretationValidation =
  | Readonly<{ kind: "accepted_for_gate_b_evaluation"; proposal: DerivedInterpretationProposal }>
  | Readonly<{
      kind: "rejected";
      reason: "source_missing" | "source_not_visible" | "wrong_agent" |
        "wrong_epoch_claim" | "invalid_confidence" | "contradicts_invariant_fixture";
    }>;
```

Provenance is required but never treated as proof that `text` faithfully represents its sources.

## Store and transaction port

```ts
export type StoreError =
  | Readonly<{ kind: "conflict"; message: string }>
  | Readonly<{ kind: "busy"; message: string }>
  | Readonly<{ kind: "integrity_failure"; message: string }>
  | Readonly<{ kind: "migration_failure"; message: string }>
  | Readonly<{ kind: "io_failure"; message: string }>;

export interface GateAUnitOfWork {
  appendEvent(event: DurableEvent): void;
  saveEncounter(encounter: EncounterRecord): void;
  saveUtteranceResult(result: UtteranceSubmissionResult): void;
  saveActionValidation(result: ActionValidationResult): void;
  saveDispatchResult(result: ImmediateDispatchResult): void;
  saveBehaviorEvent(event: BehaviorEvent): void;
}

export interface GateAStorePort {
  withTransaction<T>(operation: (unit: GateAUnitOfWork) => T):
    | Readonly<{ kind: "committed"; value: T }>
    | Readonly<{ kind: "rolled_back"; error: StoreError }>;
  loadRuntimeIdentity(agentId: AgentId): CharacterIdentityRecord | undefined;
  retrieveEncounters(query: EncounterQuery): readonly EncounterSearchResult[];
  reconcileUnfinished(worldId: WorldId, worldEpoch: WorldEpoch): readonly EventId[];
}

export type EncounterQuery = Readonly<{
  agentId: AgentId;
  principalId: PrincipalId;
  worldId: WorldId;
  worldEpoch: WorldEpoch;
  conversationText: string;
  limit: 5;
}>;

export type EncounterSearchResult = Readonly<{
  encounter: EncounterRecord;
  rank: number;
  matchedSourceEventIds: readonly EventId[];
}>;
```

No transaction may contain model, network, Mineflayer, pathfinding, or behavior-duration work.

## Persona package contract

```ts
export type CharacterIdentityRecord = Readonly<{
  agentId: AgentId;
  displayName: string;
  personaPackageRef: string;
  personaVersion: string;
  compiledContextSha256: string;
}>;

export type PersonaPackageRequest = Readonly<{
  kind: "load_compiled_persona";
  agentId: AgentId;
  personaPackageRef: string;
  expectedVersion: string;
  expectedSha256: string;
}>;

export type CompiledPersonaContext = Readonly<{
  kind: "compiled_persona_context";
  agentId: AgentId;
  displayName: string;
  version: string;
  sha256: string;
  voiceDirective: string;
  identityFacts: readonly string[];
  responseBoundaries: readonly string[];
  goodExampleExcerpts: readonly string[];
  badExampleExcerpts: readonly string[];
}>;

export interface ProfileSourcePort {
  load(request: PersonaPackageRequest):
    | Readonly<{ kind: "loaded"; context: CompiledPersonaContext }>
    | Readonly<{
        kind: "rejected";
        reason: "missing" | "malformed" | "version_mismatch" | "hash_mismatch";
      }>;
}
```

## Trigger and suppression

```ts
export type CognitionSuppressionReason =
  | "duplicate_source_event"
  | "coalesced_addressed_chat"
  | "cooldown_coalesced"
  | "cognition_queue_full"
  | "availability_blocked"
  | "not_cognitive_gate_a"
  | "not_addressed"
  | "unauthorized_principal"
  | "progress_not_cognitive";

export type TriggerDecision =
  | Readonly<{ kind: "accepted"; trigger: CognitionTrigger; pendingDepth: number }>
  | Readonly<{
      kind: "coalesced" | "suppressed";
      sourceEventId: EventId;
      reason: CognitionSuppressionReason;
      pendingDepth: number;
    }>;
```

## Local operator command

```ts
export type OperatorCommand =
  | Readonly<{ kind: "status"; requestId: OperatorRequestId }>
  | Readonly<{ kind: "pause" | "resume"; requestId: OperatorRequestId; agentId: AgentId }>
  | Readonly<{ kind: "stop_behavior"; requestId: OperatorRequestId; agentId: AgentId; behaviorId?: BehaviorId }>
  | Readonly<{ kind: "emergency_stop"; requestId: OperatorRequestId; agentId: AgentId }>
  | Readonly<{ kind: "shutdown"; requestId: OperatorRequestId; deadlineAt: IsoTimestamp }>
  | Readonly<{ kind: "doctor"; requestId: OperatorRequestId }>
  | Readonly<{ kind: "backup"; requestId: OperatorRequestId; destinationPath: string }>
  | Readonly<{ kind: "restore"; requestId: OperatorRequestId; sourcePath: string; separateDestinationPath: string }>
  | Readonly<{
      kind: "reset";
      requestId: OperatorRequestId;
      worldId: WorldId;
      fixtureName: string;
      confirmationToken: string;
    }>
  | Readonly<{ kind: "collect_evidence"; requestId: OperatorRequestId; runId: string }>;

export type OperatorResult =
  | Readonly<{ kind: "completed"; requestId: OperatorRequestId; message: string }>
  | Readonly<{ kind: "rejected" | "failed" | "unknown"; requestId: OperatorRequestId; reason: string }>;
```

Comprehensive correction is absent from Gate A. A future contract must use record-specific union members, expected versions, reason, provenance, and append-only audit; it cannot add an arbitrary replacement value.

## Causal telemetry

```ts
export type CausalSignal = Readonly<{
  kind: "state_transition" | "trigger_decision" | "model_run" |
    "utterance_delivery" | "action_validation" | "action_dispatch" |
    "behavior_event" | "capability_evidence" | "store_operation" |
    "component_health" | "checkpoint";
  at: IsoTimestamp;
  level: "debug" | "info" | "warn" | "error";
  agentId?: AgentId;
  principalId?: PrincipalId;
  worldId?: WorldId;
  worldEpoch?: WorldEpoch;
  worldSessionId?: WorldSessionId;
  eventId?: EventId;
  conversationId?: ConversationId;
  modelRunId?: ModelRunId;
  utteranceId?: UtteranceId;
  actionId?: ActionId;
  behaviorId?: BehaviorId;
  encounterId?: EncounterId;
  reasonCode: string;
  message: string;
}>;
```

Telemetry text is redacted before the sink. It never includes credentials, hidden reasoning, arbitrary other-agent context, or vendor request dumps.
