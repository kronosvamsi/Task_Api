import argparse
import requests

BASE_URL = 'http://127.0.0.1:8000/api/'

def create_item(id,name, description):
    response = requests.post(f"{BASE_URL}create/", json={'id':id, 'name': name, 'description': description})
    
    if response.status_code == 201:
        print("Item created:", response.json())
    else:
        print("Failed to create item:", response.status_code, response.text)

def list_items():
    response = requests.get(f"{BASE_URL}items/")
    print("res :",response)
    if response.status_code == 200:
        items = response.json()
        print("Items:")
        for item in items:
            print(f"{item['id']}: {item['name']} - {item['description']}")
    else:
        print("Failed to retrieve items:", response.status_code, response.text)

def update_item(item_id, name, description):
    response = requests.put(f"{BASE_URL}update/{item_id}", json={'name': name, 'description': description})
    if response.status_code == 200:
        print("Item updated:", response.json())
    else:
        print("Failed to update item:", response.status_code, response.text)

def delete_item(item_id):
    response = requests.delete(f"{BASE_URL}delete/{item_id}")
    if response.status_code == 204:
        print("Item deleted successfully.")
    else:
        print("Failed to delete item:", response.status_code, response.text)


def main():
    parser = argparse.ArgumentParser(description='CLI tool for Django REST API')
    subparsers = parser.add_subparsers(dest='command')

    # Create item command
    create_parser = subparsers.add_parser('create', help='Create a new item')
    create_parser.add_argument('id', type=int, help='Id  of the item')
    create_parser.add_argument('name', type=str, help='Name of the item')
    create_parser.add_argument('description', type=str, help='Description of the item')

    # List items command
    list_parser = subparsers.add_parser('list', help='List all items')

    # Update item command
    update_parser = subparsers.add_parser('update', help='Update an existing item')
    update_parser.add_argument('item_id', type=int, help='ID of the item to update')
    update_parser.add_argument('name', type=str, help='New name of the item')
    update_parser.add_argument('description', type=str, help='New description of the item')

    # Delete item command
    delete_parser = subparsers.add_parser('delete', help='Delete an existing item')
    delete_parser.add_argument('item_id', type=int, help='ID of the item to delete')

    args = parser.parse_args()

    if args.command == 'create':
        create_item(args.id,args.name, args.description)
    elif args.command == 'list':
        list_items()
    elif args.command == 'update':
        update_item(args.item_id, args.name, args.description)
    elif args.command == 'delete':
        delete_item(args.item_id)
    else:
        parser.print_help()


if __name__ =="__main__":
    main()
