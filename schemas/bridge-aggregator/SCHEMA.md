# Bridge Aggregator

Standard table definitions for bridge aggregator protocols that route users across different bridge protocols.

## Version: 1.0.0-alpha

### Tokens

List of tokens supported by the bridge aggregator.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| chain_id                 | The blockchain ID where the token resides.                | int |
| token_address            | The contract address of the token.                        | string |
| token_name               | The name of the token.                                    | string |
| token_symbol             | The symbol of the token.                                  | string |
| decimals                 | The decimal places of the token.                          | string |

### Token Snapshot

Snapshot of token-level metrics in the aggregator.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the snapshot.                            | timestamp |
| block_date               | The timestamp truncated (ie, YYYY-MM-DD format for daily snapshots). | date |
| chain_id                 | The blockchain ID where the token resides.                | int |
| token_address            | The contract address of the token.                        | string |
| volume_amount            | The total volume of the token bridged, decimal normalized. | double |
| volume_usd               | The total volume in USD.                                  | double |
| fees                     | The fees collected in token amount, decimal normalized.   | double |
| fees_usd                 | The fees collected in USD.                                | double |
| incentive_amount         | The amount of incentives distributed, decimal normalized. | double |
| incentive_usd            | The amount of incentives distributed in USD.              | double |

### Bridge Transactions

Transaction-level data for bridge aggregator operations.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the transaction.                         | timestamp |
| source_chain_id          | The source chain ID.                                      | int |
| destination_chain_id     | The destination chain ID.                                 | int |
| source_transaction_hash  | The transaction hash on the source chain.                 | string |
| destination_transaction_hash | The transaction hash on the destination chain.            | string |
| source_user_address      | The user's address on the source chain.                   | string |
| destination_user_address | The user's address on the destination chain.              | string |
| input_tokens             | Array of token addresses used as input.                   | [string] |
| input_token_amounts      | Array of input token amounts, decimal normalized.         | [double] |
| input_token_fees         | Array of fees paid in input tokens, decimal normalized.   | [double] |
| output_tokens            | Array of token addresses received as output.              | [string] |
| output_token_amounts     | Array of output token amounts, decimal normalized.        | [double] |

> Note: This markdown file is auto-generated.
