from datetime import datetime

from py4me.other_models.custom_field import CustomField
from py4me.serialization import Model


class Request(Model):
    _fields = {
        'addressed': bool,
        'agile_board': 'AgileBoard',
        'agile_board_column': 'AgileBoardColumn',
        'agile_board_column_position': int,
        'ci': 'ConfigurationItem',
        'checked_items': list[str],
        'completion_reason': 'RequestCompletionReason',
        'custom_fields': list[CustomField],
        'custom_fields_attachments': list['Attachment'],
        'downtime_end_at': datetime,
        'downtime_start_at': datetime,
        'desired_completion_at': datetime,
        'grouped_into': 'Request',
        'impact': 'RequestImpact',
        'internal_note': str,
        'internal_note_attachments': list['Attachment'],
        'knowledge_article': 'KnowledgeArticle',
        'major_incident_status': 'MajorIncidentStatus',
        'member': 'Person',
        'note': str,
        'note_attachments': list['Attachment'],
        'planned_effort': int,
        'problem': 'Problem',
        'product_backlog': 'ProductBacklog',
        'product_backlog_position': int,
        'project': 'Project',
        'provider_not_accountable': bool,
        'reservation': 'Reservation',
        'reviewed': bool,
        'service_instance': 'ServiceInstance',
        'source': str,
        'sourceID': str,
        'status': 'RequestStatus',
        'supplier': 'Organization',
        'supplier_requestID': str,
        'task': 'Task',
        'template': 'RequestTemplate',
        'time_spent': int,
        'time_spent_effort_class': 'EffortClass',
        'urgent': bool,
        'waiting_until': datetime,
        'workflow': 'Workflow',
        'assignemnt_count': int,
        'attachments': list['Attachment'],
        'completed_at': datetime,
        'created_at': datetime,
        'feedback': dict,
        'feedback_on_knowledge_article': 'KnowledgeArticle',
        'grouping': 'RequestGrouping',
        'id': int,
        'new_assignment': bool,
        'next_target_at': datetime,
        'organization': 'Organization',
        'provider_was_not_accountable': bool,
        'reopen_count': int,
        'resolution_duration': int,
        'resolution_target_at': datetime,
        'response_target_at': datetime,
        'satifaction': 'RequestSatisfaction',
        'support_domain': str,
        'updated_at': datetime,
        'category': 'RequestCategory',
        'created_by': 'Person',
        'requested_by': 'Person',
        'requested_for': 'Person',
        'requestor_resolution_target_at': datetime,
        'subject': str,
        'team': 'Team',
    }
    _required_fields = {

    }

    _readonly_fields = {
        'assignemnt_count': int,
        'attachments': list['Attachment'],
        'completed_at': datetime,
        'created_at': datetime,
        'feedback': dict,
        'feedback_on_knowledge_article': 'KnowledgeArticle',
        'grouping': 'RequestGrouping',
        'id': int,
        'created_by': 'Person',
        'new_assignment': bool,
        'next_target_at': datetime,
        'organization': 'Organization',
        'provider_was_not_accountable': bool,
        'reopen_count': int,
        'resolution_duration': int,
        'resolution_target_at': datetime,
        'response_target_at': datetime,
        'satifaction': 'RequestSatisfaction',
        'support_domain': str,
        'updated_at': datetime,
    }

    _validation = {
    }
