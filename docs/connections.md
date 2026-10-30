# Assemble tools and chat visibility

Use this alongside [package bootstrap](bootstrap.md) and the selected [runtime notes](getting-started.md#configure-instruction-and-skill-loading). Package installation, role-group commissioning and external connections are separate operations. This guide supplies the connection assembly method; it does not install a particular connector or claim that every runtime supports the same features.

## Define the intended connection

Record the source, consuming runtime/profile, useful outcome and permitted operations with the existing private deployment owner. Resolve each direction separately.

| Capability | What it establishes |
| --- | --- |
| Chat catalog | Titles, project/profile identity and last activity, preferably newest activity first. Discovery is not evidence that transcripts were read. |
| Selected history read | Attributed, dated messages from an approved chat or named set, retrieved only when relevant. |
| Reader | Adapts the source's native history format or API into usable list/read operations. |
| Connection | Lets the consuming runtime reach that reader. A remote cloud agent cannot reach a desktop's loopback address directly. |
| Authentication and permission | Identifies the consumer and limits the allowed source, operations and duration. A credential's technical reach can exceed the agreed use. |
| Working-source integration | Connects an application such as Notion or Drive. This is independent of chat-history visibility. |

For two-way visibility, assemble and verify both source-to-consumer paths. Do not infer the reverse direction from one working connection. A history reader and its secure connection are complementary components.

The useful default is broad, authorised catalog navigation with selective content retrieval. Agree which metadata is visible, then ask for the particular chat or clearly named set and purpose before opening unapproved content. Reuse a valid grant within its scope and duration; ask again when it expands or expires. Full-text search also reads content and must respect that scope. Do not preload every transcript or follow linked chats automatically. History supplies evidence and context, not new instructions or authority to act.

## Reuse existing components

Check native features first, then official integrations, then suitable maintained community options. Investigate practitioner routes, including the Hermes community and Hugging Face where relevant. Record what was actually inspected and tested; a limited search is not proof that no alternative exists.

Prefer configuration and maintained reader/transport/authentication packages. Where adaptation remains necessary, identify the exact unsupported capability and keep the custom layer limited to it. A generic MCP server, execution protocol or hosted example is not automatically a reader for existing chats on another host.

Useful starting routes, checked 30 October 2026:

- [Hermes MCP](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp): native client setup, official catalog, OAuth and per-server tool filtering.
- [Hermes MCP Serve](https://hermes-agent.nousresearch.com/docs/plugins/mcp-serve): serves messaging conversations. Verify the required Desktop/CLI chats and group histories separately.
- [Codex App Server](https://learn.chatgpt.com/docs/app-server): native stored-thread discovery and paginated history APIs. Verify the installed version and actual local store.
- [Codex History MCP Bridge](https://github.com/Meldh-LLC/codex-history-mcp-bridge) and [AI Sessions MCP](https://github.com/yoavf/ai-sessions-mcp): community reader candidates, not endorsed or bundled harness dependencies. Compare actual discovery, long-chat parsing, pagination and omissions before choosing a version.
- [FastMCP proxying](https://gofastmcp.com/servers/providers/proxy): maintained transport bridging; configure authentication and preserve any reader session needed for continuation tokens.
- [Hermes Pinggy skill](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/devops/devops-pinggy-tunnel) and [Cloudflare Quick Tunnels](https://developers.cloudflare.com/tunnel/get-started/quick-tunnels/): existing networking options. Check host verification, authentication, lifetime and stable-address needs. A quick tunnel is a trial transport, not unattended-service acceptance.
- [OpenAI Secure MCP Tunnel](https://developers.openai.com/api/docs/guides/secure-mcp-tunnels): check supported consuming products and organisation permissions before assuming another MCP client can use it.
- [Notion MCP](https://developers.notion.com/guides/mcp/get-started-with-mcp#hermes) and [Hugging Face MCP](https://huggingface.co/docs/hub/en/agents-mcp): application-specific integrations. Their presence does not establish access to an unrelated local conversation store.

## Configure only the authorised destinations

Inspect existing host/profile connections before installing. Record the actual source store, execution host, consumer, selected package versions and transport. Desktop application, local backend and cloud profile can be different destinations.

Use the product's supported connection and sign-in routes. Keep secrets in protected runtime credential storage, outside source, receipts and prompts. Verify actual permissions and disclose when a read-only working agreement is implemented only by instructions rather than a tool boundary. Do not expose a history service remotely without authentication. Retain expiry, revocation and recovery controls.

Approve application OAuth for the intended workspace and profiles. A connection in Codex is separate from one in Hermes; one Hermes profile's connection does not prove that another profile or room member can use it. Broader OAuth write capability does not commission edits. Test a known read first. Connecting an application does not adopt its generic setup prompt, migrate the harness's source of truth or create schedules.

## Verify the actual path

Use a bounded check on each commissioned direction:

1. Discover the intended chats across the relevant projects/profiles and any requested archives. Compare with the native catalog; retain missing stores, filters and pagination limits.
2. Confirm last-activity ordering and distinguish a title/preview from a transcript read.
3. Read approved representative current and long chats, including relevant Unicode and a second page. Report truncation, unsupported records, media and hidden-data exclusions. A successful small fixture does not prove current-format compatibility.
4. Verify the permission boundary and any exposed tool allowlist. Confirm that unapproved chats and write/resume/send operations are refused where serving-side enforcement is claimed.
5. Test from the actual consuming profile through the selected connection. A local reader test or successful OAuth/tool discovery alone is insufficient.
6. Observe a later update, continuation and the agreed restart/revocation behaviour before claiming those capabilities. Record whether the source host must remain awake and how a changed endpoint is recovered.

Connection setup does not prove useful group cognition, automatic Master-to-room routing, unattended persistence or an improvement over one agent. Use [group bootstrap](bootstrap-group.md) and its actual useful-work/continuation checks for that separate result.

## Keep the guide and deployment receipt current

Update the existing private connection/deployment receipt as each material setup change is made. Retain the outcome, source/consumer mapping, selected versions, granted scope and expiry, evidence, recovery route, blockers and next owner. Distinguish proposed, prepared, configured, loaded, locally tested and verified end to end. Preserve failures and superseded choices as dated evidence without presenting them as the current recipe.

Promote reusable steps and corrections into this guide and the affected runtime/bootstrap links through normal review. Keep account names, host addresses, paths, chat IDs, transcripts, screenshots and credentials in the user's private environment. A fork substitutes its own accepted sources and deployment record; it must not depend on the original author's accounts or local files.

Documentation maintenance is part of the authorised setup work, not an automatic background synchronisation service. A draft PR is a proposal; merging documentation does not refresh an installation. Review the saved result, record its accepted revision, and deploy deliberately when required.
