# ERC-20

Table definitions for the ERC-20 schema. These tables can be used for any protocol.

## Version: 1.0.0-alpha

### Token ERC-20 Transfers

ERC-20 Token Transfers

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The UNIX timestamp of the block associated with the transaction. | timestamp |
| block_number             | The block number for the transaction                      | bigint |
| chain_id                 | The standard chain id.                                    | int |
| from_user_address        | The address of the user sending the erc-20 transfer.      | string |
| to_user_address          | The address of the user receiving the erc-20 transfer.    | string |
| token_transfer_amount    | The amount of the token transferred (decimal normalized). | double |
| token_address            | The smart contract address of the token.                  | string |
| token_symbol             | The symbol of the token we are getting the balance of.    | string |
| log_index                | The event log. For transactions that don't emit event, create arbitrary index starting from 0. | bigint |
| transaction_hash         | The hash of the transaction.                              | string |

> Note: This markdown file is auto-generated.
