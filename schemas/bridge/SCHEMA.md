# Bridge

Standard table definitions for bridge protocols, including pool-based, mint-based, and intent-based bridges.

## Version: 1.0.0-alpha

### Tokens

List of tokens in bridge protocols.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| token_address            | The contract address of the token.                        | string |
| token_symbol             | The symbol of the token.                                  | string |
| token_decimals           | The decimal amount of the token.                          | string |
| chain_id                 | The blockchain ID where the token resides.                | int |

### Pools

List of pools in bridge protocols (applicable for pool and mint based bridges).

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp this pool was created.                      | timestamp |
| creation_block_number    | The block number this pool was created on.                | bigint |
| token_address            | The contract address of the token being bridged or pooled. | string |
| token_index              | (Optional, only applicable to pool-based) The index of the pooled token in the smart contract. | bigint |
| token_symbol             | The symbol of the token.                                  | string |
| fee_rate                 | The fee rate as a percentage for the pool, if applicable (ie, 2.3% fee as 0.023). | double |
| pool_address             | The contract address of the pool.                         | string |
| chain_id                 | Standard chain ID (ie, the chain ID of the network the pool lives on). | int |
| bridge_type              | The type of bridge (ie, pool-based, mint-based, or intent-based). | string |

### LP Snapshot

List of liquidity providers in pool-based bridge protocols.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the snapshot.                            | timestamp |
| block_date               | The timestamp truncated (ie, YYYY-MM-DD format for daily snapshots and YYYY-MM-DD HH:00:00 for hourly snapshots). | date |
| pool_address             | The address of the pool.                                  | string |
| lp_address               | The address of the liquidity provider.                    | string |
| token_address            | The contract address of the token supplied.               | string |
| token_index              | The index in the smart contract of this token, default to 0. | bigint |
| token_amount             | The amount of the supplied token, decimal normalized.     | double |
| token_amount_usd         | The amount supplied, in USD.                              | double |
| chain_id                 | The standard chain ID where the liquidity provider resides. | int |
| bridge_type              | The type of bridge (pool-based, mint-based, or intent-based). | string |

### User Snapshot

User level snapshot of accounts that have used the bridge (applicable to pool and intent based bridges).

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the snapshot.                            | timestamp |
| block_date               | The timestamp truncated (ie, YYYY-MM-DD format for daily snapshots and YYYY-MM-DD HH:00:00 for hourly snapshots). | date |
| pool_address             | (Optional, only applicable to pool-based) The contract address of the pool. | string |
| user_address             | The address of the user this snapshot activity is based on. | string |
| amount_in_usd            | The amount of tokens received on this network by the user in USD during the given snapshot. | double |
| amount_out_usd           | The amount of tokens sent out of this network by the user in USD during the given snapshot. | double |
| chain_id                 | The standard chain ID where the bridger resides.          | int |
| bridge_type              | The type of bridge (pool-based, mint-based, or intent-based). | string |

### Pool Snapshot

Pool level snapshots for pool and mint based bridges.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the snapshot.                            | timestamp |
| block_date               | The timestamp truncated (ie, YYYY-MM-DD format for daily snapshots and YYYY-MM-DD HH:00:00 for hourly snapshots). | date |
| pool_address             | The contract address of the pool.                         | string |
| token_address            | The contract address of the token being bridged or pooled. | string |
| token_index              | (Optional, only applicable to pool-based) The index of the pooled token in the smart contract. | bigint |
| token_symbol             | The symbol of the token.                                  | string |
| token_amount             | The amount of the supplied token (in a pool-based bridge), decimal normalized. | double |
| token_amount_usd         | The amount supplied, in USD.                              | double |
| volume_usd               | The bridged volume in USD, during this snapshot.          | double |
| fees_usd                 | The fees collected in USD, during the snapshot period.    | double |
| chain_id                 | The standard chain ID where the pool resides.             | int |
| bridge_type              | The type of bridge (pool-based, mint-based, or intent-based). | string |

### Bridge Transactions

List of bridge transactions.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the transaction.                         | timestamp |
| block_number             | The block number of the transaction.                      | bigint |
| transaction_hash         | The hash of the transaction this bridge originated from.  | string |
| log_index                | The log index of the transaction.                         | bigint |
| source_chain_id          | The source standard chain ID.                             | int |
| destination_chain_id     | The destination standard chain ID.                        | int |
| user_address             | The address of the user initiating the transaction.       | string |
| token_address            | The smart contract address of the source chain bridge token. | string |
| token_amount             | The amount of the token sent out from the source chain, decimal normalized. | double |
| token_amount_usd         | The token amount in USD.                                  | double |
| solver_address           | The address of the solver (for intent-based bridges).     | string |
| pool_address             | The address of the pool (for pool-based and mint-based bridges). | string |
| bridge_type              | The type of bridge (pool-based, mint-based, or intent-based). | string |

### Maker Snapshot

List of makers in intent-based bridge protocols.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the snapshot.                            | timestamp |
| block_date               | The timestamp truncated (ie, YYYY-MM-DD format for daily snapshots and YYYY-MM-DD HH:00:00 for hourly snapshots). | date |
| user_address             | The address of the maker.                                 | string |
| token_address            | The smart contract address of the token being supplied by the maker. | string |
| token_in_amount          | The amount of the token received, decimal normalized.     | double |
| amount_in_usd            | The amount received in USD, during this snapshot.         | double |
| token_out_amount         | The amount of the token sent out, decimal normalized.     | double |
| amount_out_usd           | The amount sent in USD, during this given snapshot.       | double |
| fees_usd                 | The fees collected in USD, during this snapshot.          | double |
| chain_id                 | The standard chain ID where the maker resides.            | int |

### Taker Snapshot

List of takers in intent-based bridge protocols.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the snapshot.                            | timestamp |
| block_date               | The timestamp truncated (ie, YYYY-MM-DD format for daily snapshots and YYYY-MM-DD HH:00:00 for hourly snapshots). | date |
| user_address             | The address of the taker.                                 | string |
| token_address            | The smart contract address of the token.                  | string |
| volume_amount            | The amount of volume bridged from the source chain, decimal normalized. | double |
| volume_usd               | The volume bridged in USD, in the given snapshot.         | double |
| chain_id                 | The standard chain ID where the taker resides.            | int |

### Token Snapshot

Snapshot of token level data.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the snapshot.                            | timestamp |
| block_date               | The timestamp truncated (ie, YYYY-MM-DD format for daily snapshots and YYYY-MM-DD HH:00:00 for hourly snapshots). | date |
| token_address            | he contract address of the token.                         | string |
| token_amount             | The amount of the token held in the pool, decimal normalized (for pool-based bridges). | double |
| token_amount_usd         | The amount held in USD.                                   | double |
| volume_amount            | The amount of volume bridged of the token, decimal normalized. | double |
| volume_usd               | The volume in USD, during the given period.               | double |
| total_fees_usd           | The fees collected in USD, during this given period.      | double |
| chain_id                 | The standard chain ID where the token resides.            | int |

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
