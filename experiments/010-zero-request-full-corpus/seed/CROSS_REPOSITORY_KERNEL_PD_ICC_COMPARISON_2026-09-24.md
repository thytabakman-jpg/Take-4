# Cross-Repository Kernel / PD / ICC Comparison

Date: 2026-09-24

## Goal

Record the current observed relationship between the four repositories, their root kernel definitions, PD, and ICC/controller references.

This is a descriptive snapshot of the repositories as inspected on 2026-09-24. It does not by itself promote, modify, or authorize any kernel, controller, runtime, or architecture.

## Results

| Repository | Root KERNEL.yaml | PD in kernel architecture | ICC / IC in kernel architecture | Current role indicated by kernel |
| --- | --- | --- | --- | --- |
| Reaserch | No comparable root KERNEL.yaml found | Not established by a root kernel | Not established by a root kernel | Larger legacy/authority architecture; not directly comparable by the same root-kernel convention |
| Take-2 | Yes | Yes | No explicit ICC/controller declaration in KERNEL.yaml | bootstrap_candidate |
| Take-3 | Yes | No | No | experimental_only clean-room bootstrap candidate |
| Take-4 | Yes | No explicit PD declaration | Yes, IC-022 is declared as controller_candidate | experimental_only informed-reconstruction bootstrap candidate |

## Evidence

### Take-2

The root `KERNEL.yaml` declares:

```yaml
kernel: take_2
status: bootstrap_candidate
legacy_authority: thytabakman-jpg/Reaserch
principles:
  - pd_is_epistemic_kernel
```

Therefore Take-2 explicitly incorporates PD into its kernel architecture as the epistemic kernel.

No explicit ICC/controller declaration was observed in the Take-2 root `KERNEL.yaml`.

### Take-3

The root `KERNEL.yaml` declares:

```yaml
experiment: take_3_clean_room
status: BOOTSTRAP_CANDIDATE
authority: experimental_only
```

No explicit PD or ICC/controller declaration was observed in this kernel.

### Take-4

The root `KERNEL.yaml` declares:

```yaml
experiment: take_4_informed_reconstruction
status: BOOTSTRAP_CANDIDATE
authority: experimental_only
external_corpora:
  reaserch: thytabakman-jpg/Reaserch
  take_2: thytabakman-jpg/Take-2
controller_candidate: IC-022
promoted_runtime_external: IC-2026-09-23-018
```

Therefore Take-4 explicitly connects IC-022 to the kernel architecture as a controller candidate. The kernel also distinguishes that controller candidate from the external promoted runtime.

No explicit PD-as-kernel declaration was observed in the Take-4 root `KERNEL.yaml`.

### Reaserch

No root `KERNEL.yaml` comparable to Take-2, Take-3, or Take-4 was found. Reaserch contains a substantially larger collection of architecture, runtime, workflow, policy, state, and Improvement Core materials.

Take-2 identifies Reaserch as its `legacy_authority`, and Take-4 identifies it as an external corpus.

Because Reaserch does not use the same root-kernel convention, this report does not infer that it has neither PD nor ICC. The narrower finding is that their kernel integration cannot be established by the same `KERNEL.yaml` test used for Take-2 through Take-4.

## Architectural comparison

The repositories currently provide three distinct experimental configurations:

1. Take-2 tests a kernel architecture with PD explicitly designated as its epistemic kernel.
2. Take-3 provides a clean-room kernel with neither PD nor ICC explicitly embedded.
3. Take-4 tests a kernel architecture connected to an ICC/IC controller candidate.

No inspected root kernel currently combines both an explicit PD epistemic-kernel declaration and an explicit ICC/controller declaration.

## Important distinction

The Take-4 evidence establishes that kernel, controller, and runtime are separate architectural roles:

- kernel: the `KERNEL.yaml` architecture
- controller candidate: `IC-022`
- promoted runtime external: `IC-2026-09-23-018`

Therefore the statement "Take-4 has ICC in the kernel" is best read as "the kernel explicitly references an IC controller candidate," not "ICC and the kernel are identical."

## Status

Observed snapshot only. No repository architecture was changed as part of the inspection that produced these findings.
