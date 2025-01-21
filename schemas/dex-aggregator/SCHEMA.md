# DEX Aggregator

Standard table definitions for DEX aggregators.

## Version: 1.0.0-alpha

### Tokens

List of tokens supported by the protocol.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| chain_id                 | The standard id of the chain.                             | int |
| token_address            | The contract address of the token.                        | string |
| token_name               | The full name of the token, from the eth_call name().     | string |
| token_symbol             | The symbol of the token, from the eth_call symbol().      | string |
| decimals                 | The decimals name of the token, from the eth_call decimals(). | string |

### Token Snapshot

Volume, fees, and incentives data at the token level.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the record.                              | timestamp |
| block_date               | The timestamp truncated (ie, YYYY-MM-DD format for daily snapshots and YYYY-MM-DD HH:00:00 for hourly snapshots). | date |
| chain_id                 | The standard id of the chain.                             | int |
| token_address            | The contract address of the token.                        | string |
| volume_amount            | The volume amount of the token, during the snapshot period, decimal normalized. | double |
| volume_usd               | The volume of the token in USD.                           | double |
| fees                     | The fees (ie, revenue generated from trading this token) from this token in native, decimal normalized terms. | double |
| fees_usd                 | The fees collected in USD.                                | double |
| incentive_amount         | The amount of incentives collected from this token, during the snapshot period, decimal normalized. | double |
| incentive_usd            | The value of incentives in USD.                           | double |

### Protocol Snapshot

Volume and fees data at the protocol level.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the block this snapshot was taken.       | timestamp |
| block_date               | The timestamp truncated (ie, YYYY-MM-DD format for daily snapshots and YYYY-MM-DD HH:00:00 for hourly snapshots). | date |
| chain_id                 | The standard id of the chain.                             | int |
| volume_usd               | The volume in USD, in the given snapshot period.          | double |
| fees_usd                 | The fees (ie, total revenue generated in the protocol) collected in USD, during the snapshot period. | double |

### Trades

List of trades executed on the protocol.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the trade.                               | timestamp |
| chain_id                 | The standard id of the chain this trade belongs to.       | int |
| block_number             | The block number in which the trade occurred.             | bigint |
| transaction_hash         | The transaction hash associated with this trade.          | string |
| log_index                | The event log. For transactions that don't emit event, create arbitrary index starting from 0. | bigint |
| fees                     | The amount of fees from this trade (ie, the revenue generated from executing this trade). | double |
| fees_usd                 | The fees for this trade in USD.                           | double |
| slippage                 | (Optional) The slippage of the given trade, as a percentage (ie, 1.3% slippage is 0.013). | double |
| user_address             | The address of the user initiating the trade.             | string |
| input_tokens             | The contract address of the input token(s).               | [string] |
| input_token_amounts      | Parallel array to input_tokens, dictating the normalized native amounts of each token traded. | [double] |
| output_tokens            | The contract address of the output token(s).              | [string] |
| output_token_amounts     | Parallel array to output_tokens, dictating the normalized native amounts of each token traded. | [double] |
| swap_amount_usd          | The value of the swap in USD.                             | double |

### Incentive Claim Data

Transactional data on user level incentives claimed data.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the claim.                               | timestamp |
| chain_id                 | The standard chain id.                                    | int |
| transaction_hash         | The hash of the transaction.                              | string |
| log_index                | The event log. For transactions that don't emit event, create arbitrary index starting from 0. | bigint |
| transaction_signer       | The address of the account that signed the transaction.   | string |
| user_address             | The address of the user who claimed the incentives (could be different from the transaction_signer). | string |
| claimed_token_address    | The smart contract address of the claimed token.          | string |
| amount                   | The amount of the token claimed, decimal normalized.      | double |
| amount_usd               | The amount of claimed tokens in USD.                      | double |
| other_incentive_usd      | (Optional) Any incentives outside of the claimed token, in this transaction, summed up in USD terms. | double |

> Note: This markdown file is auto-generated.
