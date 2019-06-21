"""Sublime Text plugin to remove a folder from a project easily."""

import sublime
import sublime_plugin


class ProjectRemoveFolderCommand(sublime_plugin.TextCommand):
    """The Sublime Text plugin class."""

    project_folders = []

    def run(self, _):
        """Main function which is called when the plugin is activated."""

        self.project_folders = sublime.active_window().folders()

        if not self.project_folders:
            sublime.status_message('There are no folders added to the current window.')
            return

        sublime.active_window().show_quick_panel(self.project_folders, self.remove_folder)

    def remove_folder(self, folder_index):
        """Function which removes the chosen folder from the window."""

        if folder_index == -1:
            # No folder was chosen
            return

        project_data = sublime.active_window().project_data()
        if not project_data:
            sublime.status_message('There are no folders added to the current window.')
            return

        # Iterate over a copy of the list
        for folder in list(project_data.get('folders', [])):
            if folder.get('path') == self.project_folders[folder_index]:
                project_data['folders'].remove(folder)

        sublime.active_window().set_project_data(project_data)
        sublime.active_window().status_message('"{}" removed from project'.format(self.project_folders[folder_index]))
