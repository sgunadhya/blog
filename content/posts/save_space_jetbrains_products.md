
+++
title = "Save Disk Space when Installing Jetbrains Products"
date = 2020-11-14T13:07:10+05:30
tags = ["productivity", "disk space", "intellij"]
categories = ["productivity"]
author = "Sushant Srivastava"
description = "Save Disk Space when Installing Jetbrains Products"
draft = false
+++

I am a fan of Intellij Products. I use them for coding in my personal and professional projects.
I have bought a subscription for the entire suite of Intellij Products. Those who bought the suite
will know that the suite comes with a "Toolbox" app. The "Toolbox" app keeps the line of products installed
on the computer up-to-date. Off late, I saw that disk space used by Intellij Suite grew exponentially. 

{{< figure src="/images/SettingsLocation.png" class="mid">}}

The Toolbox App keeps older versions of the installable saved to disk. The Older versions of the installable
are saved on disk as a rollback safety mechanism. The toolbox rolls back the install to an older version if the newer version has any issues. 
This was excessive checkpointing in my case.
I checked the setting, which saves only the latest version of the Installable.

{{< figure src="/images/Recommendations.png" class="mid">}}
You can save additional disk space by changing the location where the Toolbox app saves the installable. In my case, I changed it to an external drive. You can find this setting by going to the Toolbox app, then click on the octagonal-gear-like icon. This will open the 
Settings Tab. You can find the configuration by clicking on the "Tools" section of the accordion.

I hope this is helpful to anyone looking for the disk space problem with the Intellij Toolbox.

