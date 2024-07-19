# Lending / MM (Money Market) / CDP

Standard table definitions for lending protocols.

## Schema

### Pools

| Property                | Description                                                                   | Type   |
|-------------------------|-------------------------------------------------------------------------------|--------|
| protocol_name           | The name of the protocol this table belongs to.                               | string |
| chain_id                | The standard id of the chain.                                                 | number |
| creation_block_number   | The block this pool was created in.                                           | number |
| creation_timestamp      | The timestamp of the block that this pool was created in.                     | number |
| underlying_token_address| The contract address of the underlying token.                                 | string |
| underlying_token_symbol | The symbol of the underlying token.                                           | string |
| receipt_token_address   | The contract address of the receipt token.                                    | string |
| receipt_token_symbol    | The symbol of the receipt token.                                              | string |
| pool_address            | The contract address of the pool.                                             | string |
| pool_type               | The type of the pool (collateral_only, isolated, supply_pool, cdp).           | string |

### Position Snapshot

| Property                | Description                                                                   | Type   |
|-------------------------|-------------------------------------------------------------------------------|--------|
| timestamp               | The timestamp of the snapshot.                                                | string |
| protocol_name           | The name of the protocol this table belongs to.                               | string |
| chain_id                | The standard id of the chain.                                                 | number |
| pool_address            | The contract address of the pool.                                             | string |
| underlying_token_address| The contract address of the underlying token.                                 | string |
| underlying_token_symbol | The symbol of the underlying token.                                           | string |
| user_address            | The address of the user who has the position.                                 | string |
| supplied_amount         | The amount supplied by the user in native terms, normalized by underlying decimals. | number |
| supplied_amount_usd     | (Optional) The supplied amount in USD.                                        | number |
| borrowed_amount         | The amount borrowed by the user normalized to native terms, using underlying decimals. | number |
| borrowed_amount_usd     | (Optional) The borrowed amount in USD.                                        | number |
| collateral_amount       | (Optional) The amount of collateral-only tokens of this asset, normalized.    | number |
| collateral_amount_usd   | (Optional) The amount of collateral-only tokens in USD.                       | number |

### Pool Snapshot

| Property                | Description                                                                   | Type   |
|-------------------------|-------------------------------------------------------------------------------|--------|
| timestamp               | The timestamp of the snapshot.                                                | string |
| protocol_name           | The name of the protocol this table belongs to.                               | string |
| chain_id                | The standard id of the chain.                                                 | number |
| pool_address            | The contract address of the pool.                                             | string |
| underlying_token_address| The contract address of the underlying token.                                 | string |
| underlying_token_symbol | The symbol of the underlying token.                                           | string |
| underlying_token_price_usd | (Optional) The token price of the underlying asset in USD.                 | number |
| available_amount        | The amount of token's available to borrow (liquidity or net supply or supply - borrow). | number |
| available_amount_usd    | The available amount of token's in this pool in USD.                          | number |
| supplied_amount         | The total amount of the underlying token supplied in this pool normalized.    | number |
| supplied_amount_usd     | The supplied amount in USD.                                                   | number |
| non_recursive_supplied_amount | (Optional) The amount of non recursive supply in this pool, in the underlying token, decimal normalized. This is an aggregation of all of the user's net supply of this asset. | number |
| collateral_amount       | (Optional) The amount of collateral only tokens in this pool.                 | number |
| collateral_amount_usd   | (Optional) The amount of collateral only tokens in the pool.                  | number |
| collateral_factor       | The collateral factor of the pool (defined as a percentage, between 0-100).   | number |
| supply_index            | The supply index of the pool.                                                 | number |
| supply_apr              | The current annual percentage rate for supplied amount.                       | number |
| borrowed_amount         | The amount of underlying tokens borrowed from this pool, normalized to the underlying token. | number |
| borrowed_amount_usd     | The borrowed amount in USD.                                                   | number |
| borrow_index            | The borrow index of the pool.                                                 | number |
| borrow_apr              | The annual percentage rate for borrow.                                        | number |
| fees_usd                | (Optional) The total revenue / fees accrued in this pool during the given snapshot period. | number |
