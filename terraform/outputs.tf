# Sample outputs from terraform apply.
# Actual outputs might vary based on resource naming.
#
# application_insights_connection_string = <sensitive>

output "application_insights_connection_string" {
  value       = azurerm_application_insights.appinsights.connection_string
  description = "Connection String for Application Insights. Set this as APPLICATIONINSIGHTS_CONNECTION_STRING in your .env file."
  sensitive   = true
}
