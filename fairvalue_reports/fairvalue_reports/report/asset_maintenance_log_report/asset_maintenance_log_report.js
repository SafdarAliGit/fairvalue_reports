
frappe.query_reports["Asset Maintenance Log Report"] = {
    "filters": [

        {
            "fieldname": "maintenance_status",
            "label": __("Maintenance Status"),
            "fieldtype": "Select",
            "width": "100",
            "options": ["Planned", "Completed", "Cancelled", "Overdue"],
            "default": ""
        }

    ]
};

