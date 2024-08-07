# Lending / MM / CDP[^1]

[^1]: This markdown file is auto-generated.Standard table definitions for lending protocols.

## Version: 1.0.0

### Pools

List of pools in the lending protocol.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| chain_id                 | The standard id of the chain.                             | number |
| creation_block_number    | The block this pool was created in.                       | number |
| creation_timestamp       | The timestamp of the block that this pool was created in. | number |
| underlying_token_address | The contract address of the underlying token.             | string |
| underlying_token_symbol  | The symbol of the underlying token.                       | string |
| receipt_token_address    | The contract address of the receipt token.                | string |
| receipt_token_symbol     | The symbol of the receipt token.                          | string |
| pool_address             | The contract address of the pool.                         | string |
| pool_type                | The type of the pool (collateral_only, isolated, supply_pool, cdp). | string |

### Position Snapshot

Snapshot of user positions in the lending protocol.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the snapshot.                            | number |
| chain_id                 | The standard id of the chain.                             | number |
| pool_address             | The contract address of the pool.                         | string |
| underlying_token_address | The contract address of the underlying token.             | string |
| underlying_token_symbol  | The symbol of the underlying token.                       | string |
| user_address             | The address of the user who has the position.             | string |
| supplied_amount          | The amount supplied by the user in the underlying token, decimal normalized. | number |
| supplied_amount_usd      | (Optional) The supplied amount in USD.                    | number |
| borrowed_amount          | The amount borrowed by the user in the underlying token, decimal normalized. | number |
| borrowed_amount_usd      | (Optional) The borrowed amount in USD.                    | number |
| collateral_amount        | (Optional) The amount of collateral-only tokens of this asset, decimal normalized. | number |
| collateral_amount_usd    | (Optional) The amount of collateral-only tokens in USD.   | number |

### Pool Snapshot

Snapshot of the pool's state in the lending protocol.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the snapshot.                            | number |
| chain_id                 | The standard id of the chain.                             | number |
| pool_address             | The contract address of the pool.                         | string |
| underlying_token_address | The contract address of the underlying token.             | string |
| underlying_token_symbol  | The symbol of the underlying token.                       | string |
| underlying_token_price_usd | (Optional) The token price of the underlying asset in USD. | number |
| available_amount         | The amount of token's available to borrow (liquidity or net supply or supply - borrow). | number |
| available_amount_usd     | (Optional) The available amount of token's in this pool in USD. | number |
| supplied_amount          | The total amount of the underlying token supplied in this pool, decimal normalized. | number |
| supplied_amount_usd      | (Optional) The supplied amount in USD.                    | number |
| non_recursive_supplied_amount | The amount of non recursive supply in this pool, in the underlying token, decimal normalized. This is an aggregation of all of the user's net supply of this asset. | number |
| collateral_amount        | (Optional) The amount of collateral only tokens in this pool. | number |
| collateral_amount_usd    | (Optional) The amount of collateral only tokens in the pool. | number |
| collateral_factor        | The collateral factor of the pool (defined as a decimal percentage, between 0-100). | number |
| supply_index             | The supply index of the pool.                             | number |
| supply_apr               | The current annual percentage rate for supplied amount, as a decimal percentage. | number |
| borrowed_amount          | The amount of underlying tokens borrowed from this pool in the underlying token, decimal normalized. | number |
| borrowed_amount_usd      | (Optional) The borrowed amount in USD.                    | number |
| borrow_index             | The borrow index of the pool.                             | number |
| borrow_apr               | The current annual percentage rate for borrow, as a decimal percentage. | number |
| total_fees_usd           | (Optional) The total revenue or fees accrued in this pool during the given snapshot period (ie, user_fees_usd + protocol_fees_usd = total_fees_usd). | number |
| user_fees_usd            | (Optional) The portion of total revenue or fees accrued to users of the protocol during the given snapshot period. | number |
| protocol_fees_usd        | (Optional) The portion of total revenue or fees accrued to protocol during the given snapshot period. | number |

