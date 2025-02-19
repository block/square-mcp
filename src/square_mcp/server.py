from typing import Dict, Any, Optional, List
from square.client import Client
import os
from datetime import datetime

from mcp.server.fastmcp import FastMCP
from mcp.shared.exceptions import McpError
from mcp.types import ErrorData, INTERNAL_ERROR, INVALID_PARAMS

# Initialize Square client
access_token = os.getenv('SQUARE_ACCESS_TOKEN')
environment = os.getenv('SQUARE_ENVIRONMENT', 'sandbox')  # Default to sandbox if not set

if not access_token:
    raise McpError(
        ErrorData(code=INVALID_PARAMS, message="SQUARE_ACCESS_TOKEN environment variable is required")
    )

if environment not in ['sandbox', 'production']:
    raise McpError(
        ErrorData(code=INVALID_PARAMS, message="SQUARE_ENVIRONMENT must be either 'sandbox' or 'production'")
    )

square_client = Client(
    access_token=access_token,
    environment=environment
)

mcp = FastMCP(
    "square",
    title="Square MCP",
    description="Square API Model Context Protocol Server",
    version="0.1.0",
)

@mcp.tool()
async def payments(
    operation: str,
    params: Dict[str, Any]
) -> Dict[str, Any]:
    """Manage payment operations using Square API

    Args:
        operation: The operation to perform. Valid operations:
            Payments:
                - list_payments
                - create_payment
                - get_payment
                - update_payment
                - cancel_payment
            Refunds:
                - refund_payment
                - list_refunds
                - get_refund
            Disputes:
                - list_disputes
                - retrieve_dispute
                - accept_dispute
                - create_dispute_evidence
            Gift Cards:
                - create_gift_card
                - link_customer_to_gift_card
                - retrieve_gift_card
                - list_gift_cards
            Bank Accounts:
                - list_bank_accounts
                - get_bank_account
        params: Dictionary of parameters for the specific operation
    """
    try:
        if operation == "list_payments":
            result = square_client.payments.list_payments(**params)
        elif operation == "create_payment":
            result = square_client.payments.create_payment(params)
        elif operation == "refund_payment":
            result = square_client.refunds.refund_payment(params)
        elif operation == "list_disputes":
            result = square_client.disputes.list_disputes(**params)
        elif operation == "create_gift_card":
            result = square_client.gift_cards.create_gift_card(params)
        elif operation == "list_bank_accounts":
            result = square_client.bank_accounts.list_bank_accounts(**params)
        else:
            raise McpError(INVALID_PARAMS, ErrorData(message=f"Invalid operation: {operation}"))

        return result.body
    except Exception as e:
        raise McpError(INTERNAL_ERROR, ErrorData(message=str(e)))

@mcp.tool()
async def terminal(
    operation: str,
    params: Dict[str, Any]
) -> Dict[str, Any]:
    """Manage Square Terminal operations

    Args:
        operation: The operation to perform. Valid operations:
            Checkout:
                - create_terminal_checkout
                - search_terminal_checkouts
                - get_terminal_checkout
                - cancel_terminal_checkout
            Devices:
                - create_terminal_device
                - get_terminal_device
                - search_terminal_devices
            Refunds:
                - create_terminal_refund
                - search_terminal_refunds
                - get_terminal_refund
                - cancel_terminal_refund
        params: Dictionary of parameters for the specific operation
    """
    try:
        if operation == "create_terminal_checkout":
            result = square_client.terminal.create_terminal_checkout(params)
        elif operation == "create_terminal_device":
            result = square_client.terminal.create_terminal_device(params)
        elif operation == "create_terminal_refund":
            result = square_client.terminal.create_terminal_refund(params)
        else:
            raise McpError(INVALID_PARAMS, ErrorData(message=f"Invalid operation: {operation}"))

        return result.body
    except Exception as e:
        raise McpError(INTERNAL_ERROR, ErrorData(message=str(e)))

@mcp.tool()
async def orders(
    operation: str,
    params: Dict[str, Any]
) -> Dict[str, Any]:
    """Manage orders and checkout operations

    Args:
        operation: The operation to perform. Valid operations:
            Orders:
                - create_order
                - batch_retrieve_orders
                - calculate_order
                - clone_order
                - search_orders
                - pay_order
                - update_order
            Checkout:
                - create_checkout
                - create_payment_link
            Custom Attributes:
                - upsert_order_custom_attribute
                - list_order_custom_attribute_definitions
        params: Dictionary of parameters for the specific operation
    """
    try:
        if operation == "create_order":
            result = square_client.orders.create_order(params)
        elif operation == "search_orders":
            result = square_client.orders.search_orders(params)
        elif operation == "create_checkout":
            result = square_client.checkout.create_checkout(params)
        else:
            raise McpError(INVALID_PARAMS, ErrorData(message=f"Invalid operation: {operation}"))

        return result.body
    except Exception as e:
        raise McpError(INTERNAL_ERROR, ErrorData(message=str(e)))

@mcp.tool()
async def catalog(
    operation: str,
    params: Dict[str, Any]
) -> Dict[str, Any]:
    """Manage catalog operations

    Args:
        operation: The operation to perform. Valid operations:
            - create_catalog_object
            - batch_delete_catalog_objects
            - batch_retrieve_catalog_objects
            - batch_upsert_catalog_objects
            - create_catalog_image
            - delete_catalog_object
            - retrieve_catalog_object
            - search_catalog_objects
            - update_catalog_object
            - update_item_modifier_lists
            - update_item_taxes
        params: Dictionary of parameters for the specific operation
    """
    try:
        if operation == "create_catalog_object":
            result = square_client.catalog.create_catalog_object(params)
        elif operation == "search_catalog_objects":
            result = square_client.catalog.search_catalog_objects(params)
        elif operation == "batch_upsert_catalog_objects":
            result = square_client.catalog.batch_upsert_catalog_objects(params)
        else:
            raise McpError(INVALID_PARAMS, ErrorData(message=f"Invalid operation: {operation}"))

        return result.body
    except Exception as e:
        raise McpError(INTERNAL_ERROR, ErrorData(message=str(e)))

@mcp.tool()
async def inventory(
    operation: str,
    params: Dict[str, Any]
) -> Dict[str, Any]:
    """Manage inventory operations

    Args:
        operation: The operation to perform. Valid operations:
            - batch_change_inventory
            - batch_retrieve_inventory_changes
            - batch_retrieve_inventory_counts
            - retrieve_inventory_adjustment
            - retrieve_inventory_changes
            - retrieve_inventory_count
            - retrieve_inventory_physical_count
            - retrieve_inventory_transfer
        params: Dictionary of parameters for the specific operation
    """
    try:
        if operation == "batch_change_inventory":
            result = square_client.inventory.batch_change_inventory(params)
        elif operation == "retrieve_inventory_count":
            result = square_client.inventory.retrieve_inventory_count(**params)
        else:
            raise McpError(INVALID_PARAMS, ErrorData(message=f"Invalid operation: {operation}"))

        return result.body
    except Exception as e:
        raise McpError(INTERNAL_ERROR, ErrorData(message=str(e)))

@mcp.tool()
async def subscriptions(
    operation: str,
    params: Dict[str, Any]
) -> Dict[str, Any]:
    """Manage subscription operations

    Args:
        operation: The operation to perform. Valid operations:
            - create_subscription
            - search_subscriptions
            - retrieve_subscription
            - update_subscription
            - cancel_subscription
            - list_subscription_events
            - pause_subscription
            - resume_subscription
            - swap_plan
        params: Dictionary of parameters for the specific operation
    """
    try:
        if operation == "create_subscription":
            result = square_client.subscriptions.create_subscription(params)
        elif operation == "search_subscriptions":
            result = square_client.subscriptions.search_subscriptions(params)
        else:
            raise McpError(INVALID_PARAMS, ErrorData(message=f"Invalid operation: {operation}"))

        return result.body
    except Exception as e:
        raise McpError(INTERNAL_ERROR, ErrorData(message=str(e)))

@mcp.tool()
async def invoices(
    operation: str,
    params: Dict[str, Any]
) -> Dict[str, Any]:
    """Manage invoice operations

    Args:
        operation: The operation to perform. Valid operations:
            - create_invoice
            - search_invoices
            - get_invoice
            - update_invoice
            - cancel_invoice
            - publish_invoice
            - delete_invoice
        params: Dictionary of parameters for the specific operation
    """
    try:
        if operation == "create_invoice":
            result = square_client.invoices.create_invoice(params)
        elif operation == "search_invoices":
            result = square_client.invoices.search_invoices(params)
        else:
            raise McpError(INVALID_PARAMS, ErrorData(message=f"Invalid operation: {operation}"))

        return result.body
    except Exception as e:
        raise McpError(INTERNAL_ERROR, ErrorData(message=str(e)))

@mcp.tool()
async def team(
    operation: str,
    params: Dict[str, Any]
) -> Dict[str, Any]:
    """Manage team operations

    Args:
        operation: The operation to perform. Valid operations:
            Team Members:
                - create_team_member
                - bulk_create_team_members
                - update_team_member
                - retrieve_team_member
                - search_team_members
            Wages:
                - retrieve_wage_setting
                - update_wage_setting
            Labor:
                - create_break_type
                - create_shift
                - search_shifts
                - update_shift
                - create_workweek_config
            Cash Drawers:
                - list_cash_drawer_shifts
                - retrieve_cash_drawer_shift
        params: Dictionary of parameters for the specific operation
    """
    try:
        if operation == "create_team_member":
            result = square_client.team.create_team_member(params)
        elif operation == "search_team_members":
            result = square_client.team.search_team_members(params)
        elif operation == "create_shift":
            result = square_client.labor.create_shift(params)
        else:
            raise McpError(INVALID_PARAMS, ErrorData(message=f"Invalid operation: {operation}"))

        return result.body
    except Exception as e:
        raise McpError(INTERNAL_ERROR, ErrorData(message=str(e)))

@mcp.tool()
async def customers(
    operation: str,
    params: Dict[str, Any]
) -> Dict[str, Any]:
    """Manage customer operations

    Args:
        operation: The operation to perform. Valid operations:
            Customers:
                - list_customers
                - create_customer
                - delete_customer
                - retrieve_customer
                - update_customer
                - search_customers
            Groups:
                - create_customer_group
                - delete_customer_group
                - list_customer_groups
                - retrieve_customer_group
                - update_customer_group
            Segments:
                - list_customer_segments
                - retrieve_customer_segment
            Custom Attributes:
                - create_customer_custom_attribute_definition
                - delete_customer_custom_attribute_definition
                - list_customer_custom_attribute_definitions
        params: Dictionary of parameters for the specific operation
    """
    try:
        if operation == "create_customer":
            result = square_client.customers.create_customer(params)
        elif operation == "search_customers":
            result = square_client.customers.search_customers(params)
        elif operation == "create_customer_group":
            result = square_client.customer_groups.create_customer_group(params)
        else:
            raise McpError(INVALID_PARAMS, ErrorData(message=f"Invalid operation: {operation}"))

        return result.body
    except Exception as e:
        raise McpError(INTERNAL_ERROR, ErrorData(message=str(e)))

@mcp.tool()
async def loyalty(
    operation: str,
    params: Dict[str, Any]
) -> Dict[str, Any]:
    """Manage loyalty operations

    Args:
        operation: The operation to perform. Valid operations:
            Programs:
                - create_loyalty_program
                - retrieve_loyalty_program
            Accounts:
                - create_loyalty_account
                - search_loyalty_accounts
                - retrieve_loyalty_account
                - accumulate_loyalty_points
                - adjust_loyalty_points
                - search_loyalty_events
            Promotions:
                - create_loyalty_promotion
                - cancel_loyalty_promotion
        params: Dictionary of parameters for the specific operation
    """
    try:
        if operation == "create_loyalty_program":
            result = square_client.loyalty.create_loyalty_program(params)
        elif operation == "create_loyalty_account":
            result = square_client.loyalty.create_loyalty_account(params)
        else:
            raise McpError(INVALID_PARAMS, ErrorData(message=f"Invalid operation: {operation}"))

        return result.body
    except Exception as e:
        raise McpError(INTERNAL_ERROR, ErrorData(message=str(e)))

@mcp.tool()
async def bookings(
    operation: str,
    params: Dict[str, Any]
) -> Dict[str, Any]:
    """Manage booking operations

    Args:
        operation: The operation to perform. Valid operations:
            Bookings:
                - create_booking
                - search_bookings
                - retrieve_booking
                - update_booking
                - cancel_booking
            Team Member Bookings:
                - bulk_retrieve_team_member_bookings
                - retrieve_team_member_booking_profile
            Location Profiles:
                - list_location_booking_profiles
                - retrieve_location_booking_profile
            Custom Attributes:
                - create_booking_custom_attribute_definition
                - update_booking_custom_attribute_definition
        params: Dictionary of parameters for the specific operation
    """
    try:
        if operation == "create_booking":
            result = square_client.bookings.create_booking(params)
        elif operation == "search_bookings":
            result = square_client.bookings.search_bookings(params)
        else:
            raise McpError(INVALID_PARAMS, ErrorData(message=f"Invalid operation: {operation}"))

        return result.body
    except Exception as e:
        raise McpError(INTERNAL_ERROR, ErrorData(message=str(e)))

@mcp.tool()
async def business(
    operation: str,
    params: Dict[str, Any]
) -> Dict[str, Any]:
    """Manage business operations

    Args:
        operation: The operation to perform. Valid operations:
            Merchants:
                - list_merchants
                - retrieve_merchant
            Locations:
                - list_locations
                - create_location
                - retrieve_location
                - update_location
            Vendors:
                - bulk_create_vendors
                - bulk_retrieve_vendors
                - create_vendor
                - search_vendors
                - update_vendor
            Sites:
                - list_sites
        params: Dictionary of parameters for the specific operation
    """
    try:
        if operation == "list_locations":
            result = square_client.locations.list_locations()
        elif operation == "create_location":
            result = square_client.locations.create_location(params)
        elif operation == "create_vendor":
            result = square_client.vendors.create_vendor(params)
        else:
            raise McpError(INVALID_PARAMS, ErrorData(message=f"Invalid operation: {operation}"))

        return result.body
    except Exception as e:
        raise McpError(INTERNAL_ERROR, ErrorData(message=str(e)))
