# NFT Schema

This is OpenBlock Labs standard NFT schema.

## Schema

### NFT Transfers

**Description:** List of NFT transfers.

| Property               | Description                                | Type   |
|------------------------|--------------------------------------------|--------|
| timestamp              | The timestamp of the transfer.             | number |
| block_number           | The block number of the transfer.          | number |
| transaction_id         | The transaction id of the transfer here.   | string |
| nft_collection_address | The contract address of the NFT collection.| string |
| nft_id                 | The unique identifier of the NFT.          | string |
| sender_address         | The address of the sender of the NFT.      | string |
| receiver_address       | The address of the receiver of the NFT.    | string |