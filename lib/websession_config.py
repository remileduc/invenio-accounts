# -*- coding: utf-8 -*-
##
## $Id$
##
## This file is part of CDS Invenio.
## Copyright (C) 2002, 2003, 2004, 2005, 2006 CERN.
##
## CDS Invenio is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## CDS Invenio is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with CDS Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

# pylint: disable-msg=C0301

"""WebSession configuration parameters."""

__revision__ = "$Id$"

CFG_WEBSESSION_GROUP_JOIN_POLICY = {'VISIBLEOPEN': 'VO',
                                    'VISIBLEMAIL': 'VM',
                                    'INVISIBLEOPEN': 'IO',
                                    'INVISIBLEMAIL': 'IM'  
                                    }

CFG_WEBSESSION_USERGROUP_STATUS = {'ADMIN':  'A',
                                   'MEMBER':'M',
                                   'PENDING':'P'
                                   }

CFG_WEBSESSION_ERROR_MESSAGES = {
    'ERR_WEBSESSION_DB_ERROR': '_("Sorry there was an error with the database.")',
    'ERR_WEBSESSION_GROUP_NO_RIGHTS': '_("Sorry, You don\'t have sufficient rights on this group.")'
}

CFG_WEBSESSION_WARNING_MESSAGES = {
    'WRN_WEBSESSION_NO_GROUP_NAME': '_("Please enter a group name.")',
    'WRN_WEBSESSION_NOT_VALID_GROUP_NAME': '_("Please enter a valid group name.")',
    'WRN_WEBSESSION_GROUP_NAME_EXISTS': '_("Group name already exists. Please choose another group name.")',
    'WRN_WEBSESSION_NO_JOIN_POLICY': '_("Please choose a group join policy.")',
    'WRN_WEBSESSION_MULTIPLE_GROUPS': '_("Please select only one group.")',
    'WRN_WEBSESSION_NO_GROUP_SELECTED': '_("Please select one group.")',
    'WRN_WEBSESSION_GROUP_ALREADY_DELETED': '_("The group has already been deleted.")',
    'WRN_WEBSESSION_ALREADY_MEMBER': '_("You are already member of the group.")',
    'WRN_WEBSESSION_NO_MEMBER_SELECTED': '_("Please choose a member if you want to remove him from the group.")',
    'WRN_WEBSESSION_NO_USER_SELECTED_ADD': '_("Please choose a user from the list if you want him to be added to the group.")',
    'WRN_WEBSESSION_ALREADY_MEMBER_ADD': '_("The user is already member of the group.")',
    'WRN_WEBSESSION_ALREADY_MEMBER_REJECT': '_("The user request for joining group has already been rejected.")', 
    'WRN_WEBSESSION_NO_USER_SELECTED_DEL': '_("Please choose a user from the list if you want him to be removed from waiting list.")'
}

CFG_WEBSESSION_INFO_MESSAGES = {"GROUP_CREATED": '_("You have successfully created a new group.")',
                                "JOIN_GROUP": '_("You have successfully joined a new group.")',
                                "GROUP_UPDATED": '_("You have successfully updated a group.")',
                                "GROUP_DELETED": '_("You have successfully deleted a group.")',
                                "MEMBER_DELETED": '_("You have successfully deleted a member.")',
                                "MEMBER_ADDED": '_("You have successfully added a new member.")',
                                "MEMBER_REJECTED": '_("You have successfully removed a waiting member from the list.")',
                                "JOIN_REQUEST": '_("The group administrator has been notified of your request.")',
                                "LEAVE_GROUP": '_("You have successfully left a group.")'
                               
}