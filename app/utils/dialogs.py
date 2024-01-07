import Cocoa


def file_open_dialog() -> str:
    panel = Cocoa.NSOpenPanel.openPanel()
    panel.setCanCreateDirectories_(False)
    panel.setCanChooseDirectories_(False)
    panel.setCanChooseFiles_(True)
    panel.setResolvesAliases_(True)
    panel.setAllowsMultipleSelection_(False)
    panel.setAllowsOtherFileTypes_(True)
    panel.setFloatingPanel_(True)
    # panel.setOneShot_(True)
    # panel.setReleasedWhenClosed_(True)
    panel.center()
    panel.setTitle_("Укажите файл с таблицей подписчиков")
    # panel.setMessage_("Укажите файл с таблицей подписчиков")
    # panel.setNameFieldLabel_("Файл с таблицей подписчиков")
    # if panel.runModal() == Cocoa.NSOKButton:
    if (
        panel.runModalForDirectory_file_types_("~/Downloads", None, ["csv"])
        == Cocoa.NSFileHandlingPanelOKButton
        # == Cocoa.NSOKButton
    ):
        return panel.filename()
    return ""
