local Device = require("device")
Device.supportsScreensaver = function() return true end
Device.powerd:initWakeupMgr()
