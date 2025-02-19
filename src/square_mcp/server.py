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
        match operation:
            # Payments
            case "list_payments":
                result = square_client.payments.list_payments(**params)
            case "create_payment":
                result = square_client.payments.create_payment(params)
            case "get_payment":
                result = square_client.payments.get_payment(**params)
            case "update_payment":
                result = square_client.payments.update_payment(**params)
            case "cancel_payment":
                result = square_client.payments.cancel_payment(**params)
            # Refunds
            case "refund_payment":
                result = square_client.refunds.refund_payment(params)
            case "list_refunds":
                result = square_client.refunds.list_payment_refunds(**params)
            case "get_refund":
                result = square_client.refunds.get_payment_refund(**params)
            # Disputes
            case "list_disputes":
                result = square_client.disputes.list_disputes(**params)
            case "retrieve_dispute":
                result = square_client.disputes.retrieve_dispute(**params)
            case "accept_dispute":
                result = square_client.disputes.accept_dispute(**params)
            case "create_dispute_evidence":
                result = square_client.disputes.create_dispute_evidence(**params)
            # Gift Cards
            case "create_gift_card":
                result = square_client.gift_cards.create_gift_card(params)
            case "link_customer_to_gift_card":
                result = square_client.gift_cards.link_customer_to_gift_card(**params)
            case "retrieve_gift_card":
                result = square_client.gift_cards.retrieve_gift_card(**params)
            case "list_gift_cards":
                result = square_client.gift_cards.list_gift_cards(**params)
            # Bank Accounts
            case "list_bank_accounts":
                result = square_client.bank_accounts.list_bank_accounts(**params)
            case "get_bank_account":
                result = square_client.bank_accounts.get_bank_account(**params)
            case _:
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
        match operation:
            # Checkout
            case "create_terminal_checkout":
                result = square_client.terminal.create_terminal_checkout(params)
            case "search_terminal_checkouts":
                result = square_client.terminal.search_terminal_checkouts(params)
            case "get_terminal_checkout":
                result = square_client.terminal.get_terminal_checkout(**params)
            case "cancel_terminal_checkout":
                result = square_client.terminal.cancel_terminal_checkout(**params)
            # Devices
            case "create_terminal_device":
                result = square_client.terminal.create_terminal_device(params)
            case "get_terminal_device":
                result = square_client.terminal.get_terminal_device(**params)
            case "search_terminal_devices":
                result = square_client.terminal.search_terminal_devices(params)
            # Refunds
            case "create_terminal_refund":
                result = square_client.terminal.create_terminal_refund(params)
            case "search_terminal_refunds":
                result = square_client.terminal.search_terminal_refunds(params)
            case "get_terminal_refund":
                result = square_client.terminal.get_terminal_refund(**params)
            case "cancel_terminal_refund":
                result = square_client.terminal.cancel_terminal_refund(**params)
            case _:
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
        match operation:
            # Orders
            case "create_order":
                result = square_client.orders.create_order(params)
            case "batch_retrieve_orders":
                result = square_client.orders.batch_retrieve_orders(params)
            case "calculate_order":
                result = square_client.orders.calculate_order(params)
            case "clone_order":
                result = square_client.orders.clone_order(params)
            case "search_orders":
                result = square_client.orders.search_orders(params)
            case "pay_order":
                result = square_client.orders.pay_order(params)
            case "update_order":
                result = square_client.orders.update_order(**params)
            # Checkout
            case "create_checkout":
                result = square_client.checkout.create_checkout(params)
            case "create_payment_link":
                result = square_client.checkout.create_payment_link(params)
            # Custom Attributes
            case "upsert_order_custom_attribute":
                result = square_client.orders.upsert_order_custom_attribute(**params)
            case "list_order_custom_attribute_definitions":
                result = square_client.orders.list_order_custom_attribute_definitions(**params)
            case _:
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
        match operation:
            case "create_catalog_object":
                result = square_client.catalog.create_catalog_object(params)
            case "batch_delete_catalog_objects":
                result = square_client.catalog.batch_delete_catalog_objects(params)
            case "batch_retrieve_catalog_objects":
                result = square_client.catalog.batch_retrieve_catalog_objects(params)
            case "batch_upsert_catalog_objects":
                result = square_client.catalog.batch_upsert_catalog_objects(params)
            case "create_catalog_image":
                result = square_client.catalog.create_catalog_image(params)
            case "delete_catalog_object":
                result = square_client.catalog.delete_catalog_object(**params)
            case "retrieve_catalog_object":
                result = square_client.catalog.retrieve_catalog_object(**params)
            case "search_catalog_objects":
                result = square_client.catalog.search_catalog_objects(params)
            case "update_catalog_object":
                result = square_client.catalog.update_catalog_object(**params)
            case "update_item_modifier_lists":
                result = square_client.catalog.update_item_modifier_lists(params)
            case "update_item_taxes":
                result = square_client.catalog.update_item_taxes(params)
            case _:
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
        match operation:
            case "batch_change_inventory":
                result = square_client.inventory.batch_change_inventory(params)
            case "batch_retrieve_inventory_changes":
                result = square_client.inventory.batch_retrieve_inventory_changes(params)
            case "batch_retrieve_inventory_counts":
                result = square_client.inventory.batch_retrieve_inventory_counts(params)
            case "retrieve_inventory_adjustment":
                result = square_client.inventory.retrieve_inventory_adjustment(**params)
            case "retrieve_inventory_changes":
                result = square_client.inventory.retrieve_inventory_changes(**params)
            case "retrieve_inventory_count":
                result = square_client.inventory.retrieve_inventory_count(**params)
            case "retrieve_inventory_physical_count":
                result = square_client.inventory.retrieve_inventory_physical_count(**params)
            case "retrieve_inventory_transfer":
                result = square_client.inventory.retrieve_inventory_transfer(**params)
            case _:
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
        match operation:
            case "create_subscription":
                result = square_client.subscriptions.create_subscription(params)
            case "search_subscriptions":
                result = square_client.subscriptions.search_subscriptions(params)
            case "retrieve_subscription":
                result = square_client.subscriptions.retrieve_subscription(**params)
            case "update_subscription":
                result = square_client.subscriptions.update_subscription(**params)
            case "cancel_subscription":
                result = square_client.subscriptions.cancel_subscription(**params)
            case "list_subscription_events":
                result = square_client.subscriptions.list_subscription_events(**params)
            case "pause_subscription":
                result = square_client.subscriptions.pause_subscription(**params)
            case "resume_subscription":
                result = square_client.subscriptions.resume_subscription(**params)
            case "swap_plan":
                result = square_client.subscriptions.swap_plan(**params)
            case _:
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
        match operation:
            case "create_invoice":
                result = square_client.invoices.create_invoice(params)
            case "search_invoices":
                result = square_client.invoices.search_invoices(params)
            case "get_invoice":
                result = square_client.invoices.get_invoice(**params)
            case "update_invoice":
                result = square_client.invoices.update_invoice(**params)
            case "cancel_invoice":
                result = square_client.invoices.cancel_invoice(**params)
            case "publish_invoice":
                result = square_client.invoices.publish_invoice(**params)
            case "delete_invoice":
                result = square_client.invoices.delete_invoice(**params)
            case _:
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
        match operation:
            # Team Members
            case "create_team_member":
                result = square_client.team.create_team_member(params)
            case "bulk_create_team_members":
                result = square_client.team.bulk_create_team_members(params)
            case "update_team_member":
                result = square_client.team.update_team_member(**params)
            case "retrieve_team_member":
                result = square_client.team.retrieve_team_member(**params)
            case "search_team_members":
                result = square_client.team.search_team_members(params)
            # Wages
            case "retrieve_wage_setting":
                result = square_client.labor.retrieve_wage_setting(**params)
            case "update_wage_setting":
                result = square_client.labor.update_wage_setting(**params)
            # Labor
            case "create_break_type":
                result = square_client.labor.create_break_type(params)
            case "create_shift":
                result = square_client.labor.create_shift(params)
            case "search_shifts":
                result = square_client.labor.search_shifts(params)
            case "update_shift":
                result = square_client.labor.update_shift(**params)
            case "create_workweek_config":
                result = square_client.labor.create_workweek_config(params)
            # Cash Drawers
            case "list_cash_drawer_shifts":
                result = square_client.cash_drawers.list_cash_drawer_shifts(**params)
            case "retrieve_cash_drawer_shift":
                result = square_client.cash_drawers.retrieve_cash_drawer_shift(**params)
            case _:
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
        match operation:
            # Customers
            case "list_customers":
                result = square_client.customers.list_customers(**params)
            case "create_customer":
                result = square_client.customers.create_customer(params)
            case "delete_customer":
                result = square_client.customers.delete_customer(**params)
            case "retrieve_customer":
                result = square_client.customers.retrieve_customer(**params)
            case "update_customer":
                result = square_client.customers.update_customer(**params)
            case "search_customers":
                result = square_client.customers.search_customers(params)
            # Groups
            case "create_customer_group":
                result = square_client.customer_groups.create_customer_group(params)
            case "delete_customer_group":
                result = square_client.customer_groups.delete_customer_group(**params)
            case "list_customer_groups":
                result = square_client.customer_groups.list_customer_groups(**params)
            case "retrieve_customer_group":
                result = square_client.customer_groups.retrieve_customer_group(**params)
            case "update_customer_group":
                result = square_client.customer_groups.update_customer_group(**params)
            # Segments
            case "list_customer_segments":
                result = square_client.customer_segments.list_customer_segments(**params)
            case "retrieve_customer_segment":
                result = square_client.customer_segments.retrieve_customer_segment(**params)
            # Custom Attributes
            case "create_customer_custom_attribute_definition":
                result = square_client.customer_custom_attributes.create_customer_custom_attribute_definition(params)
            case "delete_customer_custom_attribute_definition":
                result = square_client.customer_custom_attributes.delete_customer_custom_attribute_definition(**params)
            case "list_customer_custom_attribute_definitions":
                result = square_client.customer_custom_attributes.list_customer_custom_attribute_definitions(**params)
            case _:
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
        match operation:
            # Programs
            case "create_loyalty_program":
                result = square_client.loyalty.create_loyalty_program(params)
            case "retrieve_loyalty_program":
                result = square_client.loyalty.retrieve_loyalty_program(**params)
            # Accounts
            case "create_loyalty_account":
                result = square_client.loyalty.create_loyalty_account(params)
            case "search_loyalty_accounts":
                result = square_client.loyalty.search_loyalty_accounts(params)
            case "retrieve_loyalty_account":
                result = square_client.loyalty.retrieve_loyalty_account(**params)
            case "accumulate_loyalty_points":
                result = square_client.loyalty.accumulate_loyalty_points(**params)
            case "adjust_loyalty_points":
                result = square_client.loyalty.adjust_loyalty_points(**params)
            case "search_loyalty_events":
                result = square_client.loyalty.search_loyalty_events(params)
            # Promotions
            case "create_loyalty_promotion":
                result = square_client.loyalty.create_loyalty_promotion(**params)
            case "cancel_loyalty_promotion":
                result = square_client.loyalty.cancel_loyalty_promotion(**params)
            case _:
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
        match operation:
            # Bookings
            case "create_booking":
                result = square_client.bookings.create_booking(params)
            case "search_bookings":
                result = square_client.bookings.search_bookings(params)
            case "retrieve_booking":
                result = square_client.bookings.retrieve_booking(**params)
            case "update_booking":
                result = square_client.bookings.update_booking(**params)
            case "cancel_booking":
                result = square_client.bookings.cancel_booking(**params)
            # Team Member Bookings
            case "bulk_retrieve_team_member_bookings":
                result = square_client.bookings.bulk_retrieve_team_member_bookings(params)
            case "retrieve_team_member_booking_profile":
                result = square_client.bookings.retrieve_team_member_booking_profile(**params)
            # Location Profiles
            case "list_location_booking_profiles":
                result = square_client.bookings.list_location_booking_profiles(**params)
            case "retrieve_location_booking_profile":
                result = square_client.bookings.retrieve_location_booking_profile(**params)
            # Custom Attributes
            case "create_booking_custom_attribute_definition":
                result = square_client.booking_custom_attributes.create_booking_custom_attribute_definition(params)
            case "update_booking_custom_attribute_definition":
                result = square_client.booking_custom_attributes.update_booking_custom_attribute_definition(**params)
            case _:
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
        match operation:
            # Merchants
            case "list_merchants":
                result = square_client.merchants.list_merchants(**params)
            case "retrieve_merchant":
                result = square_client.merchants.retrieve_merchant(**params)
            # Locations
            case "list_locations":
                result = square_client.locations.list_locations()
            case "create_location":
                result = square_client.locations.create_location(params)
            case "retrieve_location":
                result = square_client.locations.retrieve_location(**params)
            case "update_location":
                result = square_client.locations.update_location(**params)
            # Vendors
            case "bulk_create_vendors":
                result = square_client.vendors.bulk_create_vendors(params)
            case "bulk_retrieve_vendors":
                result = square_client.vendors.bulk_retrieve_vendors(params)
            case "create_vendor":
                result = square_client.vendors.create_vendor(params)
            case "search_vendors":
                result = square_client.vendors.search_vendors(params)
            case "update_vendor":
                result = square_client.vendors.update_vendor(**params)
            # Sites
            case "list_sites":
                result = square_client.sites.list_sites(**params)
            case _:
                raise McpError(INVALID_PARAMS, ErrorData(message=f"Invalid operation: {operation}"))

        return result.body
    except Exception as e:
        raise McpError(INTERNAL_ERROR, ErrorData(message=str(e)))
