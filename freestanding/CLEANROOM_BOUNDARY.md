# Clean-room boundary — ZRF freestanding lane

## Rule

The purpose of reading other repositories is to understand externally visible responsibilities, not to transplant their expression, source layout, scripts, templates or implementation.

```text
OBSERVATION ≠ SOURCE_IMPORT
CONCEPT ≠ CODE
BUILD_TOOL ≠ RUNTIME_DEPENDENCY
FORK_OWNERSHIP ≠ AUTHORSHIP_OF_INHERITED_CODE
```

## Observation boundary

### `runner-images_RAFCODE`

Allowed observation:

- an image has a definition, a build phase, validation and release evidence;
- architectures and image labels are explicit;
- image production and image consumption are different responsibilities.

Not imported:

- Packer templates;
- provisioning scripts;
- GitHub/Microsoft image definitions;
- folder topology;
- README wording;
- package inventories;
- release workflows.

### `actions`

Allowed observation:

- orchestration can be separated from payload logic;
- immutable revisions and provenance boundaries matter.

Not imported:

- Gradle Actions implementation;
- JavaScript/TypeScript bundles;
- action metadata layout beyond what GitHub itself requires for CI;
- upstream docs or generated distributions.

The repository already records that inherited Gradle code remains third-party; this lane preserves that boundary instead of attempting to relabel it.

### `Est-dio-de-udio`

Allowed observation:

- it is a consumer candidate for deterministic, low-level, auditable execution.

Not imported:

- DSP algorithms;
- Android application code;
- Gradle configuration;
- native/JVM modules.

## Authorial surface in this lane

The authored expression introduced here is limited to:

- the ZRF 4-bit/nibble state machine specification;
- its register/memory/state model;
- its instruction encoding and bounded branch semantics;
- the freestanding C implementation;
- minimal architecture entry adapters written directly for the target ISAs;
- linker memory map;
- build/evidence contract;
- navigation and provenance documents.

Primitive facts such as XOR, AND, OR, addition, machine opcodes, ELF concepts and CPU instruction mnemonics are not claimed as proprietary inventions.

## Gate

Any future contribution that copies or closely adapts third-party implementation must leave this clean-room lane and enter a separately classified provenance path with holder, license, obligations and evidence.
