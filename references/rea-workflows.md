# REA workflow reference

## Target routing

| Target | First route | Key boundary |
|---|---|---|
| JS/Electron directory or ASAR | `analyze_javascript_application` | Static graph; do not infer runtime behavior not observed |
| Native binary/library | `open_binary` | Provider selection is explicit; Ghidra/Hopper/IDA may be required |
| .NET PE/CLI | `inspect_managed_artifact` | Static metadata/CIL; native dependencies may remain unresolved |
| Android APK | `inspect_android_package` | JADX/JDK requirements vary; package inventory is separate |
| Firmware | region inspection, then scoped extraction | Use a new output directory and caller-supplied Binwalk/Unblob |
| Website/browser runtime | list existing browser targets | Observe only the authorized page; screenshots/network data can contain secrets |
| HAR/SAZ/PCAP/qlog | saved-capture inspection | Historical evidence is not live traffic and does not prove completeness |
| WASM | `inspect_wasm_artifact` | WAT is decoded representation, not original source |
| EVM bytecode | `inspect_evm_interface` | Select raw/hex carrier; selectors and mutability are inferred candidates |
| SQLite snapshot | `inspect_sqlite_database` | Inspect schema first; keep DB/WAL identity and note row truncation |
| Go binary | `inspect_go_binary` | Missing embedded metadata does not prove the binary is not Go |
| ELF/core/layout | offline layout or recorded-crash inspection | Historical PIDs do not select live processes |

## Evidence checklist

For every material finding record:

- target path/URL and SHA-256 where available;
- operation/tool and provider identity;
- Evidence ID and parent Evidence ID;
- exact function/module/record/node selected;
- whether the fact is observed, inferred, or unknown;
- coverage, truncation, provider, and runtime limitations;
- redactions applied to secrets or personal data;
- reproduction or validation command.

## Provider notes

- Start with default summary output for large artifacts.
- Use exact retained references for paging; do not rerun identical work solely to obtain more output.
- An empty call list with partial/unknown coverage is not proof that no calls exist.
- Static inspection does not establish execution behavior.
- Runtime capture can affect application state, files, accounts, devices, and services; scope it explicitly.
- Commercial tools such as IDA Pro, Hopper, and JEB require the user's own license and remain subject to vendor terms.

## Clean-room reconstruction pattern

1. Write a behavior specification from observations and evidence.
2. Build a fresh implementation with original names, structure, and assets.
3. Add black-box tests based on permitted inputs/outputs and documented interfaces.
4. Compare behavior, not copied implementation text or proprietary resources.
5. Keep a provenance log showing which observations informed each requirement.
