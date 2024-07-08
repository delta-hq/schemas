# NFT Schema

This is OpenBlock Labs standard NFT schema.

## Schema

### NFT Transfers

**Description:** List of NFT transfers.

| Property               | Description                                | Type   |
|------------------------|--------------------------------------------|--------|
| timestamp              | The timestamp of the transfer.             | number |
| blockNumber            | The block number of the transfer.          | number |
| transactionId          | The transaction id of the transfer here.   | string |
| nftCollectionAddress   | The contract address of the NFT collection.| string |
| nftId                  | The unique identifier of the NFT.          | string |
| senderAddress          | The address of the sender of the NFT.      | string |
| receiverAddress        | The address of the receiver of the NFT.    | string |