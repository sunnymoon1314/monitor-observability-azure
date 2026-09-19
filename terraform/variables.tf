variable "resource_group_name" {
  description = "The name of the Resource Group"
  type        = string
}

variable "location" {
  description = "The Azure Region"
  type        = string
}

variable "log_analytics_workspace_name" {
  description = "The name of the Log Analytics Workspace"
  type        = string
  default     = "law-observability-demo"
}

variable "application_insights_name" {
  description = "The name of the Application Insights instance"
  type        = string
  default     = "appi-observability-demo"
}
