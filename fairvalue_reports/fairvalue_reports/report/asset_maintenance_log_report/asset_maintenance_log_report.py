from decimal import Decimal
import frappe
from frappe import _


def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data


def get_columns():
    columns = [
        {
            "label": _("ID"),
            "fieldname": "id",
            "fieldtype": "Link",
            "options": "Asset Maintenance Log",
            "width": 120,
        },
        {
            "label": _("Status"),
            "fieldname": "status",
            "fieldtype": "Data",
            "width": 100
        },
        {
            "label": _("Asset Maintenance"),
            "fieldname": "asset_maintenance",
            "fieldtype": "Link",
            "options": "Asset Maintenance",
            "width": 120
        },
        {
            "label": _("Actions Performed"),
            "fieldname": "actions_performed",
            "fieldtype": "Data",
            "width": 120
        },
        {
            "label": _("Asset Name"),
            "fieldname": "asset_name",
            "fieldtype": "Data",
            "width": 120
        }
    ]

    return columns


def get_conditions(filters):
    conditions = []
    params = {}

    if filters.get("maintenance_status"):
        conditions.append("aml.maintenance_status = %(maintenance_status)s")
        params["maintenance_status"] = filters["maintenance_status"]

    return " AND ".join(conditions), params


def get_data(filters):
    data = []
    conditions, params = get_conditions(filters)

    # Handle case where no conditions are applied
    where_clause = f"WHERE 1=1" if not conditions else f"WHERE {conditions}"

    query = f"""
    SELECT 
        aml.name AS id,
        aml.maintenance_status AS status,
        aml.asset_maintenance,
        aml.actions_performed,
        aml.asset_name
    FROM `tabAsset Maintenance Log` AS aml
    {where_clause}
    """

    result = frappe.db.sql(query, params, as_dict=1)
    data.extend(result)
    return data
