# Automated Liquidity Management

Standard table definitions for automated liquidity management protocol.

## Version: 1.0.0-alpha

### Pools

List of pools in the protocol.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| chain_id                 | The standard chain id.                                    | int |
| timestamp                | The timestamp this pool was created.                      | timestamp |
| creation_block_number    | The block number that this pool was created.              | bigint |
| strategy_vault_contract_address | The contract address of the strategy vault which manages the liquidity pool positions. | string |
| liquidity_pool_address   | The contract address of the underlying liquidity pool where liquidity are deposited into | string |
| strategy_vault_receipt_token_address | The contract address of ERC20 token which represents the share of liquidity provided. | string |
| strategy_vault_receipt_token_decimals | The decimal amount of the ERC20 receipt token.            | int |
| strategy_vault_receipt_token_symbol | The symbol of the receipt token.                          | string |

### Position Snapshot

Snapshot of the pool users.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the snapshot.                            | timestamp |
| block_date               | The timestamp truncated (ie, YYYY-MM-DD format for daily snapshots and YYYY-MM-DD HH:00:00 for hourly snapshots). | date |
| chain_id                 | The standard chain id.                                    | int |
| strategy_vault_contract_address | The address of the strategy vault this user has a position in. | string |
| user_address             | The address of the user who has a position in the strategy vault. | string |
| liquidity_pool_address   | The address of the underlying liquidity pool where liquidity are deposited into | string |
| underlying_token_address | The address of the supplied underlying token.             | string |
| underlying_token_index   | The index of the underlying token in the smart contract, default 0. | bigint |
| underlying_token_amount  | The amount based on the user's share of the total underlying token, decimal normalized. | double |
| underlying_token_amount_usd | The amount based on the user's share of the total underlying token, in USD. | double |
| total_fees_usd           | The total amount of revenue and fees paid in this pool in the given snapshot, in USD. | double |

### Pool Snapshot

TVL, fees, and incentives data at the pool level.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the snapshot.                            | timestamp |
| block_date               | The timestamp truncated (ie, YYYY-MM-DD format for daily snapshots and YYYY-MM-DD HH:00:00 for hourly snapshots). | date |
| chain_id                 | The standard chain id.                                    | int |
| strategy_vault_contract_address | The address of the strategy vault this user has a position in. | string |
| liquidity_pool_address   | The address of the underlying liquidity pool where liquidity are deposited into | string |
| underlying_token_address | The address of the supplied underlying token.             | string |
| underlying_token_index   | The index of the underlying token in the smart contract, default 0. | bigint |
| underlying_token_amount  | The amount of underlying token supplied in this pool, decimal normalized. | double |
| underlying_token_amount_usd | The amount of underlying tokens supplied in this pool, in USD. | double |
| total_fees_usd           | The total amount of revenue and fees paid in this pool in the given snapshot, in USD. | double |

### ERC-20 LP Token Transfer Events

All LP Token transfer events

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the transaction.                         | timestamp |
| chain_id                 | The standard id of the chain.                             | int |
| block_number             | The block number of the trade.                            | bigint |
| log_index                | The event log. For transactions that don't emit event, create arbitrary index starting from 0. | bigint |
| transaction_hash         | The hash of the transaction.                              | string |
| from_address             | The from address of the event (ie, the from field in a transfer). | string |
| to_address               | The to address of the event (ie, the to field in a transfer). | string |
| pool_address             | The contract address of the pool LP token.                | string |
| amount                   | The amount of token transacted, decimal normalized.       | double |
| event_type               | The type of event, corresponds to the action taken by the user (ie, deposit, withdrawal). | string |

### Events

All user events (ie, Deposit, Withdrawal)

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the transaction.                         | timestamp |
| chain_id                 | The standard id of the chain.                             | int |
| block_number             | The block number of the trade.                            | bigint |
| log_index                | The event log. For transactions that don't emit event, create arbitrary index starting from 0. | bigint |
| transaction_hash         | The hash of the transaction.                              | string |
| user_address             | The address that initiates the transaction (ie, the transaction signer). | string |
| pool_address             | The smart contract address of the pool.                   | string |
| underlying_token_address | The contract address of the underlying token or deposited token. | string |
| amount                   | The amount of token transacted, decimal normalized.       | double |
| amount_usd               | The amount of token transacted, in USD.                   | double |
| event_type               | The type of event, corresponds to the action taken by the user (ie, deposit, withdrawal). | string |

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
