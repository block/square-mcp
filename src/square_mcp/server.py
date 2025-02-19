from typing import Dict, Any, Optional, List
from square.client import Client
import os
from datetime import datetime

from mcp.server.fastmcp import FastMCP
from mcp.shared.exceptions import McpError
from mcp.types import ErrorData, INTERNAL_ERROR, INVALID_PARAMS

# Initialize Square client
square_client = Client(
    access_token=os.getenv('SQUARE_ACCESS_TOKEN'),
    environment='sandbox'  # Change to 'production' for production environment
)

mcp = FastMCP(
    "square",
    title="Square MCP",
    description="Square API Model Context Protocol Server",
    version="0.1.0",
)

# Payment and Refund Tools
@mcp.tool("Create a payment")
async def create_payment(
    source_id: str,
    amount: int,
    currency: str,
    location_id: str,
    idempotency_key: Optional[str] = None
) -> Dict[str, Any]:
    """
    Create a payment using Square API.
    
    Args:
        source_id: The ID of the payment source (card nonce, etc.)
        amount: The payment amount in cents
        currency: The currency code (e.g., 'USD')
        location_id: The ID of the business location
        idempotency_key: Optional unique key to prevent duplicate payments
    """
    try:
        body = {
            "source_id": source_id,
            "amount_money": {
                "amount": amount,
                "currency": currency
            },
            "location_id": location_id,
            "idempotency_key": idempotency_key or str(datetime.now().timestamp())
        }
        result = square_client.payments.create_payment(body)
        return result.body
    except Exception as e:
        raise McpError(INTERNAL_ERROR, ErrorData(message=str(e)))

@mcp.tool("Refund a payment")
async def refund_payment(
    payment_id: str,
    amount: int,
    currency: str,
    reason: Optional[str] = None,
    idempotency_key: Optional[str] = None
) -> Dict[str, Any]:
    """
    Refund a payment using Square API.
    
    Args:
        payment_id: The ID of the payment to refund
        amount: The refund amount in cents
        currency: The currency code (e.g., 'USD')
        reason: Optional reason for the refund
        idempotency_key: Optional unique key to prevent duplicate refunds
    """
    try:
        body = {
            "payment_id": payment_id,
            "amount_money": {
                "amount": amount,
                "currency": currency
            },
            "reason": reason,
            "idempotency_key": idempotency_key or str(datetime.now().timestamp())
        }
        result = square_client.refunds.refund_payment(body)
        return result.body
    except Exception as e:
        raise McpError(INTERNAL_ERROR, ErrorData(message=str(e)))

# Order Tools
@mcp.tool("Create an order")
async def create_order(
    location_id: str,
    line_items: List[Dict[str, Any]],
    idempotency_key: Optional[str] = None
) -> Dict[str, Any]:
    """
    Create an order using Square API.
    
    Args:
        location_id: The ID of the business location
        line_items: List of items in the order
        idempotency_key: Optional unique key to prevent duplicate orders
    """
    try:
        body = {
            "order": {
                "location_id": location_id,
                "line_items": line_items
            },
            "idempotency_key": idempotency_key or str(datetime.now().timestamp())
        }
        result = square_client.orders.create_order(body)
        return result.body
    except Exception as e:
        raise McpError(INTERNAL_ERROR, ErrorData(message=str(e)))

# Catalog Tools
@mcp.tool("Create catalog item")
async def create_catalog_item(
    name: str,
    description: Optional[str] = None,
    price_money: Optional[Dict[str, Any]] = None,
    idempotency_key: Optional[str] = None
) -> Dict[str, Any]:
    """
    Create a catalog item using Square API.
    
    Args:
        name: The name of the item
        description: Optional description of the item
        price_money: Optional price information
        idempotency_key: Optional unique key to prevent duplicates
    """
    try:
        body = {
            "idempotency_key": idempotency_key or str(datetime.now().timestamp()),
            "object": {
                "type": "ITEM",
                "item_data": {
                    "name": name,
                    "description": description,
                    "variations": [
                        {
                            "type": "ITEM_VARIATION",
                            "item_variation_data": {
                                "name": "Regular",
                                "price_money": price_money
                            }
                        }
                    ]
                }
            }
        }
        result = square_client.catalog.create_catalog_object(body)
        return result.body
    except Exception as e:
        raise McpError(INTERNAL_ERROR, ErrorData(message=str(e)))

# Customer Tools
@mcp.tool("Create customer")
async def create_customer(
    given_name: Optional[str] = None,
    family_name: Optional[str] = None,
    email_address: Optional[str] = None,
    phone_number: Optional[str] = None,
    idempotency_key: Optional[str] = None
) -> Dict[str, Any]:
    """
    Create a customer using Square API.
    
    Args:
        given_name: Optional first name of the customer
        family_name: Optional last name of the customer
        email_address: Optional email address
        phone_number: Optional phone number
        idempotency_key: Optional unique key to prevent duplicates
    """
    try:
        body = {
            "idempotency_key": idempotency_key or str(datetime.now().timestamp()),
            "given_name": given_name,
            "family_name": family_name,
            "email_address": email_address,
            "phone_number": phone_number
        }
        result = square_client.customers.create_customer(body)
        return result.body
    except Exception as e:
        raise McpError(INTERNAL_ERROR, ErrorData(message=str(e)))

# Inventory Tools
@mcp.tool("Adjust inventory")
async def adjust_inventory(
    catalog_object_id: str,
    location_id: str,
    quantity: int,
    idempotency_key: Optional[str] = None
) -> Dict[str, Any]:
    """
    Adjust inventory counts using Square API.
    
    Args:
        catalog_object_id: The ID of the catalog item
        location_id: The ID of the business location
        quantity: The quantity to adjust (positive or negative)
        idempotency_key: Optional unique key to prevent duplicates
    """
    try:
        body = {
            "idempotency_key": idempotency_key or str(datetime.now().timestamp()),
            "changes": [
                {
                    "type": "ADJUSTMENT",
                    "adjustment": {
                        "catalog_object_id": catalog_object_id,
                        "location_id": location_id,
                        "quantity": str(quantity)
                    }
                }
            ]
        }
        result = square_client.inventory.batch_change_inventory(body)
        return result.body
    except Exception as e:
        raise McpError(INTERNAL_ERROR, ErrorData(message=str(e)))

# Location Tools
@mcp.tool("List locations")
async def list_locations() -> Dict[str, Any]:
    """
    List all locations for the business using Square API.
    """
    try:
        result = square_client.locations.list_locations()
        return result.body
    except Exception as e:
        raise McpError(INTERNAL_ERROR, ErrorData(message=str(e)))

# Team Management Tools
@mcp.tool("Create team member")
async def create_team_member(
    given_name: str,
    family_name: str,
    email_address: Optional[str] = None,
    phone_number: Optional[str] = None,
    idempotency_key: Optional[str] = None
) -> Dict[str, Any]:
    """
    Create a team member using Square API.
    
    Args:
        given_name: First name of the team member
        family_name: Last name of the team member
        email_address: Optional email address
        phone_number: Optional phone number
        idempotency_key: Optional unique key to prevent duplicates
    """
    try:
        body = {
            "idempotency_key": idempotency_key or str(datetime.now().timestamp()),
            "team_member": {
                "given_name": given_name,
                "family_name": family_name,
                "email_address": email_address,
                "phone_number": phone_number
            }
        }
        result = square_client.team.create_team_member(body)
        return result.body
    except Exception as e:
        raise McpError(INTERNAL_ERROR, ErrorData(message=str(e)))

# Payout Tools
@mcp.tool("List payouts")
async def list_payouts(
    location_id: Optional[str] = None,
    begin_time: Optional[str] = None,
    end_time: Optional[str] = None,
    sort_order: Optional[str] = None,
    cursor: Optional[str] = None
) -> Dict[str, Any]:
    """
    List payouts using Square API.
    
    Args:
        location_id: Optional ID of the location to list payouts for
        begin_time: Optional RFC 3339 timestamp for the beginning of the reporting period
        end_time: Optional RFC 3339 timestamp for the end of the reporting period
        sort_order: Optional sort order (ASC or DESC)
        cursor: Optional pagination cursor
    """
    try:
        result = square_client.payouts.list_payouts(
            location_id=location_id,
            begin_time=begin_time,
            end_time=end_time,
            sort_order=sort_order,
            cursor=cursor
        )
        return result.body
    except Exception as e:
        raise McpError(INTERNAL_ERROR, ErrorData(message=str(e)))

@mcp.tool("Get payout")
async def get_payout(
    payout_id: str
) -> Dict[str, Any]:
    """
    Get details of a specific payout using Square API.
    
    Args:
        payout_id: The ID of the payout to retrieve
    """
    try:
        result = square_client.payouts.get_payout(payout_id=payout_id)
        return result.body
    except Exception as e:
        raise McpError(INTERNAL_ERROR, ErrorData(message=str(e)))

@mcp.tool("List payout entries")
async def list_payout_entries(
    payout_id: str,
    sort_order: Optional[str] = None,
    cursor: Optional[str] = None
) -> Dict[str, Any]:
    """
    List all entries for a specific payout using Square API.
    
    Args:
        payout_id: The ID of the payout to list entries for
        sort_order: Optional sort order (ASC or DESC)
        cursor: Optional pagination cursor
    """
    try:
        result = square_client.payouts.list_payout_entries(
            payout_id=payout_id,
            sort_order=sort_order,
            cursor=cursor
        )
        return result.body
    except Exception as e:
        raise McpError(INTERNAL_ERROR, ErrorData(message=str(e)))
