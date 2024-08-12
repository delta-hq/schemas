# Bridge

Standard table definitions for bridge protocols, including pool-based, mint-based, and intent-based bridges.

## Version: 1.0.0-alpha

### Tokens

List of tokens in bridge protocols.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| token_address            | The contract address of the token.                        | string |
| token_symbol             | The symbol of the token.                                  | string |
| token_decimals           | The decimal amount of the token.                          | number |
| chain_id                 | The blockchain ID where the token resides.                | number |

### Pools

List of pools in bridge protocols (applicable for pool and mint based bridges).

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| creation_timestamp       | The timestamp this pool was created.                      | number |
| creation_block_number    | The block number this pool was created on.                | number |
| token_address            | The contract address of the token being bridged or pooled. | string |
| token_index              | (Optional, only applicable to pool-based) The index of the pooled token in the smart contract. | number |
| token_symbol             | The symbol of the token.                                  | string |
| fee_rate                 | The fee rate as a percentage for the pool, if applicable (ie, 2.3% fee as 0.023). | number |
| pool_address             | The contract address of the pool.                         | string |
| chain_id                 | Standard chain ID (ie, the chain ID of the network the pool lives on). | number |
| bridge_type              | The type of bridge (ie, pool-based, mint-based, or intent-based). | string |

### LP Snapshot

List of liquidity providers in pool-based bridge protocols.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the snapshot.                            | number |
| pool_address             | The address of the pool.                                  | string |
| lp_address               | The address of the liquidity provider.                    | string |
| token_address            | The contract address of the token supplied.               | string |
| token_index              | The index in the smart contract of this token, default to 0. | number |
| token_amount             | The amount of the supplied token, decimal normalized.     | number |
| token_amount_usd         | The amount supplied, in USD.                              | number |
| chain_id                 | The standard chain ID where the liquidity provider resides. | number |
| bridge_type              | The type of bridge (pool-based, mint-based, or intent-based). | string |

### User Snapshot

User level snapshot of accounts that have used the bridge (applicable to pool and intent based bridges).

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the snapshot.                            | number |
| pool_address             | (Optional, only applicable to pool-based) The contract address of the pool. | string |
| user_address             | The address of the user this snapshot activity is based on. | string |
| amount_in_usd            | The amount of tokens received on this network by the user in USD during the given snapshot. | number |
| amount_out_usd           | The amount of tokens sent out of this network by the user in USD during the given snapshot. | number |
| chain_id                 | The standard chain ID where the bridger resides.          | number |
| bridge_type              | The type of bridge (pool-based, mint-based, or intent-based). | string |

### Pool Snapshot

Pool level snapshots for pool and mint based bridges.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the snapshot.                            | number |
| pool_address             | The contract address of the pool.                         | string |
| token_address            | The contract address of the token being bridged or pooled. | string |
| token_index              | (Optional, only applicable to pool-based) The index of the pooled token in the smart contract. | number |
| token_symbol             | The symbol of the token.                                  | string |
| token_amount             | The amount of the supplied token (in a pool-based bridge), decimal normalized. | number |
| token_amount_usd         | The amount supplied, in USD.                              | number |
| volume_usd               | The bridged volume in USD, during this snapshot.          | number |
| fees_usd                 | The fees collected in USD, during the snapshot period.    | number |
| chain_id                 | The standard chain ID where the pool resides.             | number |
| bridge_type              | The type of bridge (pool-based, mint-based, or intent-based). | string |

### Bridge Transactions

List of bridge transactions.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the transaction.                         | number |
| block_number             | The block number of the transaction.                      | number |
| transaction_hash         | The hash of the transaction this bridge originated from.  | string |
| log_index                | The log index of the transaction.                         | number |
| source_chain_id          | The source standard chain ID.                             | number |
| destination_chain_id     | The destination standard chain ID.                        | number |
| user_address             | The address of the user initiating the transaction.       | string |
| token_address            | The smart contract address of the source chain bridge token. | string |
| token_amount             | The amount of the token sent out from the source chain, decimal normalized. | number |
| token_amount_usd         | The token amount in USD.                                  | number |
| solver_address           | The address of the solver (for intent-based bridges).     | string |
| pool_address             | The address of the pool (for pool-based and mint-based bridges). | string |
| bridge_type              | The type of bridge (pool-based, mint-based, or intent-based). | string |

### Maker Snapshot

List of makers in intent-based bridge protocols.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the snapshot.                            | number |
| user_address             | The address of the maker.                                 | string |
| token_address            | The smart contract address of the token being supplied by the maker. | string |
| token_in_amount          | The amount of the token received, decimal normalized.     | number |
| amount_in_usd            | The amount received in USD, during this snapshot.         | number |
| token_out_amount         | The amount of the token sent out, decimal normalized.     | string |
| amount_out_usd           | The amount sent in USD, during this given snapshot.       | number |
| fees_usd                 | The fees collected in USD, during this snapshot.          | number |
| chain_id                 | The standard chain ID where the maker resides.            | string |

### Taker Snapshot

List of takers in intent-based bridge protocols.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the snapshot.                            | number |
| user_address             | The address of the taker.                                 | string |
| token_address            | The smart contract address of the token.                  | string |
| volume_usd               | The volume bridged in USD, in the given snapshot.         | number |
| chain_id                 | The standard chain ID where the taker resides.            | number |

### Token Snapshot

List of takers in intent-based bridge protocols.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the snapshot.                            | number |
| token_address            | he contract address of the token.                         | string |
| token_amount             | The amount of the token held in the pool, decimal normalized (for pool-based bridges). | number |
| token_amount_usd         | The amount held in USD.                                   | number |
| volume_usd               | The volume in USD, during the given period.               | number |
| total_fees_usd           | The fees collected in USD, during this given period.      | number |
| chain_id                 | The standard chain ID where the token resides.            | number |

> Note: This markdown file is auto-generated.
