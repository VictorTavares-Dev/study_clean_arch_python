RESPONSE_GET_RESOURCE_SHARES = [
    {
        "resourceShareArn": "arn:aws:ram:us-east-1:888577041900:resource-share/8901c2d9-77f5-4f0a-803d-419c6408778c",
        "name": "LakeFormation-V3-QJHUPL73TJ",
        "owningAccountId": "888577041900",
        "allowExternalPrincipals": True,
        "status": "ACTIVE",
        "creationTime": "2025-06-15 16:29:27.813000-03:00",
        "lastUpdatedTime": "2025-06-15 16:29:27.813000-03:00",
        "featureSet": "STANDARD",
    }
]  # Implementar os outros resource shares com suas variações de permissions

RESPONSE_PERMISSIONS = {
    "arn:aws:ram:us-east-1:888577041900:resource-share/8901c2d9-77f5-4f0a-803d-419c6408778c": [
        {
            "arn": "arn:aws:ram::aws:permission/AWSRAMLFEnabledGlueTableReadWrite",
            "version": "1",
            "defaultVersion": True,
            "resourceType": "glue:Table",
            "status": "ASSOCIATED",
            "lastUpdatedTime": "2025-06-15 16:29:27.923000-03:00",
            "featureSet": "STANDARD",
        },
        {
            "arn": "arn:aws:ram::aws:permission/AWSRAMPermissionGlueTableReadWriteForCatalog",
            "version": "3",
            "defaultVersion": True,
            "resourceType": "glue:Catalog",
            "status": "ASSOCIATED",
            "lastUpdatedTime": "2025-06-15 16:29:27.979000-03:00",
            "featureSet": "STANDARD",
        },
        {
            "arn": "arn:aws:ram::aws:permission/AWSRAMPermissionGlueTableReadWriteForDatabase",
            "version": "3",
            "defaultVersion": True,
            "resourceType": "glue:Database",
            "status": "ASSOCIATED",
            "lastUpdatedTime": "2025-06-15 16:29:27.992000-03:00",
            "featureSet": "STANDARD",
        },
    ]
}  # Implementar os outros resource shares com suas variações de permissions
