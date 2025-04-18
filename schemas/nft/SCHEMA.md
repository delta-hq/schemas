# NFT

Standard table definitions for NFTs.

## Version: 1.0.0-alpha

### NFT Transfers

List of NFT transfers.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the transfer.                            | timestamp |
| chain_id                 | The standard id of the chain.                             | int |
| block_number             | The block number of the transfer.                         | bigint |
| transaction_hash         | The transaction hash of the transfer.                     | string |
| log_index                | The event log. For transactions that don't emit event, create arbitrary index starting from 0. | bigint |
| nft_collection_address   | The contract address of the NFT collection.               | string |
| nft_id                   | The unique identifier of the NFT.                         | string |
| sender_address           | The address of the sender of the NFT.                     | string |
| receiver_address         | The address of the receiver of the NFT.                   | string |

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
