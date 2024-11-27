# Bridge Aggregator

Standard table definitions for bridge aggregator protocols that route users across different bridge protocols.

## Version: 1.0.0-alpha

### Tokens

List of tokens supported by the bridge aggregator.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| chain_id                 | The blockchain ID where the token resides.                | number |
| token_address            | The contract address of the token.                        | string |
| token_name               | The name of the token.                                    | string |
| token_symbol             | The symbol of the token.                                  | string |
| decimals                 | The decimal places of the token.                          | number |

### Token Snapshot

Snapshot of token-level metrics in the aggregator.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the snapshot.                            | number |
| block_date               | The timestamp truncated (ie, YYYY-MM-DD format for daily snapshots). | date |
| chain_id                 | The blockchain ID where the token resides.                | number |
| token_address            | The contract address of the token.                        | string |
| volume_amount            | The total volume of the token bridged, decimal normalized. | number |
| volume_usd               | The total volume in USD.                                  | number |
| fees                     | The fees collected in token amount, decimal normalized.   | number |
| fees_usd                 | The fees collected in USD.                                | number |
| incentive_amount         | The amount of incentives distributed, decimal normalized. | number |
| incentive_usd            | The amount of incentives distributed in USD.              | number |

### Bridge Transactions

Transaction-level data for bridge aggregator operations.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the transaction.                         | number |
| source_chain_id          | The source chain ID.                                      | number |
| destination_chain_id     | The destination chain ID.                                 | number |
| source_transaction_hash  | The transaction hash on the source chain.                 | string |
| destination_transaction_hash | The transaction hash on the destination chain.            | string |
| source_user_address      | The user's address on the source chain.                   | string |
| destination_user_address | The user's address on the destination chain.              | string |
| input_tokens             | Array of token addresses used as input.                   | [string] |
| input_token_amounts      | Array of input token amounts, decimal normalized.         | [number] |
| input_token_fees         | Array of fees paid in input tokens, decimal normalized.   | [number] |
| output_tokens            | Array of token addresses received as output.              | [string] |
| output_token_amounts     | Array of output token amounts, decimal normalized.        | [number] |

> Note: This markdown file is auto-generated.
