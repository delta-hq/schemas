# Yield Aggregators Schema

This is OpenBlock Labs standard Yield Aggregators schema.

## Schema

### Pools
| Property                  | Description                                                          | Type   |
|---------------------------|----------------------------------------------------------------------|--------|
| chain_id                  | The standard chain id.                                               | number |
| creation_timestamp        | The timestamp this pool was created.                                 | number |
| creation_block_number     | The block number that this pool was created.                         | number |
| underlying_token_address  | The contract address of the underlying token or deposited token.     | string |
| underlying_token_index    | The index of the underlying token in the smart contract, default 0.  | number |
| underlying_token_symbol   | The symbol of the underlying token token.                            | string |
| underlying_token_decimals | The decimal amount of the underlying token.                          | number |
| receipt_token_address     | The contract address of the output or receipt token of this pool, if available.| string |
| receipt_token_symbol      | The symbol of the receipt token.                                     | string |
| receipt_token_decimals    | The symbol decimal amount for the receipt token.                     | number |
| pool_address              | The smart contract address of the pool.                              | string |
| pool_symbol               | The symbol of the pool.                                              | string |

### Position Snapshot
| Property                   | Description                                                          | Type   |
|----------------------------|----------------------------------------------------------------------|--------|
| timestamp                  | The timestamp of the snapshot.                                       | number |
| chain_id                   | The standard chain id.                                               | number |
| pool_address               | The address of the pool this user has a position in.                 | string |
| user_address               | The address of the user who has a position in the pool.              | string |
| underlying_token_address   | The address of the supplied underlying token.                        | string |
| underlying_token_index     | The index in the smart contract of this underlying token, default 0. | number |
| underlying_token_amount    | The amount of the underlying token that the user deposited, decimal normalized.| number |
| underlying_token_amount_usd| The amount of underlying tokens supplied, in USD.                    | number |
| total_fees_usd        | The total amount of revenue and fees paid in this pool in the given snapshot, in USD.      | number |

### Pool Snapshot
| Property                   | Description                                                          | Type   |
|----------------------------|----------------------------------------------------------------------|--------|
| timestamp                  | The timestamp of the snapshot.                                       | number |
| chain_id                   | The standard chain id.                                               | number |
| underlying_token_address   | The contract address of the underlying token or deposited token.     | string |
| underlying_token_index     | The index of the underlying token in the smart contract, default 0.  | number |
| pool_address               | The address of the pool.                                             | string |
| underlying_token_amount    | The amount of underlying token supplied in this pool, decimal normalized.| number |
| underlying_token_amount_usd| The amount of underlying tokens supplied in this pool, in USD.       | number |
| total_fees_usd             | The total amount of revenue and fees paid in this pool in the given snapshot, in USD.      | number |