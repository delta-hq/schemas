# Automated Liquidity Management

Standard table definitions for automated liquidity management protocol.

## Version: 1.0.0-alpha

### Pools

List of pools in the protocol.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| chain_id                 | The standard chain id.                                    | number |
| timestamp                | The timestamp this pool was created.                      | number |
| creation_block_number    | The block number that this pool was created.              | number |
| strategy_vault_contract_address | The contract address of the strategy vault which manages the liquidity pool positions. | string |
| liquidity_pool_address   | The contract address of the underlying liquidity pool where liquidity are deposited into | string |
| strategy_vault_receipt_token_address | The contract address of ERC20 token which represents the share of liquidity provided. | string |
| strategy_vault_receipt_token_decimals | The decimal amount of the ERC20 receipt token.            | number |
| strategy_vault_receipt_token_symbol | The symbol of the receipt token.                          | string |

### Position Snapshot

Snapshot of the pool users.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the snapshot.                            | number |
| block_date               | The timestamp truncated (ie, YYYY-MM-DD format for daily snapshots and YYYY-MM-DD HH:00:00 for hourly snapshots). | date |
| chain_id                 | The standard chain id.                                    | number |
| strategy_vault_contract_address | The address of the strategy vault this user has a position in. | string |
| user_address             | The address of the user who has a position in the strategy vault. | string |
| liquidity_pool_address   | The address of the underlying liquidity pool where liquidity are deposited into | string |
| underlying_token_address | The address of the supplied underlying token.             | string |
| underlying_token_index   | The index of the underlying token in the smart contract, default 0. | number |
| underlying_token_amount  | The amount based on the user's share of the total underlying token, decimal normalized. | number |
| underlying_token_amount_usd | The amount based on the user's share of the total underlying token, in USD. | number |
| total_fees_usd           | The total amount of revenue and fees paid in this pool in the given snapshot, in USD. | number |

### Pool Snapshot

TVL, fees, and incentives data at the pool level.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the snapshot.                            | number |
| block_date               | The timestamp truncated (ie, YYYY-MM-DD format for daily snapshots and YYYY-MM-DD HH:00:00 for hourly snapshots). | date |
| chain_id                 | The standard chain id.                                    | number |
| strategy_vault_contract_address | The address of the strategy vault this user has a position in. | string |
| liquidity_pool_address   | The address of the underlying liquidity pool where liquidity are deposited into | string |
| underlying_token_address | The address of the supplied underlying token.             | string |
| underlying_token_index   | The index of the underlying token in the smart contract, default 0. | number |
| underlying_token_amount  | The amount of underlying token supplied in this pool, decimal normalized. | number |
| underlying_token_amount_usd | The amount of underlying tokens supplied in this pool, in USD. | number |
| total_fees_usd           | The total amount of revenue and fees paid in this pool in the given snapshot, in USD. | number |

### Events

All user events (ie, Deposit, Withdrawal)

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the transaction.                         | number |
| chain_id                 | The standard id of the chain.                             | number |
| block_number             | The block number of the trade.                            | number |
| log_index                | The event log. For transactions that don't emit event, create arbitrary index starting from 0. | number |
| transaction_hash         | The hash of the transaction.                              | string |
| user_address             | The address that initiates the transaction (ie, the transaction signer). | string |
| pool_address             | The smart contract address of the pool.                   | string |
| underlying_token_address | The contract address of the underlying token or deposited token. | string |
| amount                   | The amount of token transacted, decimal normalized.       | number |
| amount_usd               | The amount of token transacted, in USD.                   | number |
| event_type               | The type of event, corresponds to the action taken by the user (ie, deposit, withdrawal). | string |

### Incentive Claim Data

Transactional data on user level incentives claimed data.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the claim.                               | number |
| chain_id                 | The standard chain id.                                    | number |
| transaction_hash         | The hash of the transaction.                              | string |
| log_index                | The event log. For transactions that don't emit event, create arbitrary index starting from 0. | number |
| transaction_signer       | The address of the account that signed the transaction.   | string |
| user_address             | The address of the user who claimed the incentives (could be different from the transaction_signer). | string |
| claimed_token_address    | The smart contract address of the claimed token.          | string |
| amount                   | The amount of the token claimed, decimal normalized.      | number |
| amount_usd               | The amount of claimed tokens in USD.                      | number |
| other_incentive_usd      | (Optional) Any incentives outside of the claimed token, in this transaction, summed up in USD terms. | number |

> Note: This markdown file is auto-generated.
