# Sigma-Hunting-App
A Splunk App containing Sigma detection rules, which can be updated dynamically from a Git repository.

## Motivation
Most of the modern Security Operations Center (SOC) store the detection rules in a central repository such as GitHub or GitLab as part of the Dev Sec Ops development approach. Furthermore, [Sigma](https://github.com/Neo23x0/sigma) as a generic signature description language is used in many SOCs. Updating the Sigma rules from a Sigma repository to Splunk was still a manual time-consuming task. The Sigma Hunting App solves that problem by providing a dedicated Splunk App, which can be used to dynamically update Sigma detection rules from a Git repository. The triggered detection rules are stored in a separate threat-hunting index helping the SOC Analyst in their investigations. Additionally, the Sigma Hunting App for Splunk uses information of the [Mitre ATT&CK Matrix](https://attack.mitre.org/matrices/enterprise/) to enrich the triggered detection rules.

The Sigma Hunting App for Splunk provides the following features:
- dynamically update of Sigma detection rules from a remote Git repository
- Store triggered detection rules in a dedicated index
- Enrichment of triggered detection rules with data from the [Mitre ATT&CK Matrix](https://attack.mitre.org/matrices/enterprise/)
- Providing powerfull dashboards for investigation: security posture, host investigator, APT investigator, lateral movement investigator

### Update of Sigma Detection Rules
The Sigma detection rules can be updated from the Sigma Hunting App:
![](https://github.com/P4T12ICK/Sigma-Hunting-App/blob/master/pictures/sigma_hunting_app_update.png)

The remote Git repository can be configured through the Set Up view of the Sigma Hunting App:
![](https://github.com/P4T12ICK/Sigma-Hunting-App/blob/master/pictures/sigma_hunting_app_configuration.png)


### Store triggered Detection Rules in a dedicated Index
The triggered Detection Rules are stored in the threat-hunting index:
![](https://github.com/P4T12ICK/Sigma-Hunting-App/blob/master/pictures/sigma_hunting_app_threat_hunting_index.png)

### Enrichment with Mitre ATT&CK Data
The triggered Detection Rules in the threat-hunting index are enriched with Mitre ATT&CK Data such as Technique, Tactics, ID, Threat Actors.

### Providing Investigation Dashbaords
There exist several dashbaord for investigations.
The security posture dashboard gives you an overview about the triggered detection rules categorized into Mitre ATT&CK Tactics:
![](https://github.com/P4T12ICK/Sigma-Hunting-App/blob/master/pictures/sigma_hunting_app_security_posture_dashboard.png)

The Host Investigator supports you to perfrom investigation for a specific host. It shows the different triggered detection rules in a timeline chart:
![](https://github.com/P4T12ICK/Sigma-Hunting-App/blob/master/pictures/sigma_hunting_app_host_investigator.png)

The APT investigator tries to identify, which threat actor is attacking you by using the information of the triggered detection rules:
![](https://github.com/P4T12ICK/Sigma-Hunting-App/blob/master/pictures/sigma_hunting_app_APT_investigator.png)


## Installation
Installation steps are described in detail in the [wiki](https://github.com/P4T12ICK/Sigma-Hunting-App/wiki/Installation-Sigma-Hunting-App).

## Contribution
Please report all issues, that we can improve the Sigma Hunting App together. If you have some feature request, feel free to add them and we will figure it out together.

## Credits
This is a private repository developed by Patrick Bareiss (Twitter: [@bareiss_patrick](https://twitter.com/bareiss_patrick)).

## Thank you
I need to say thank you to some people, who supported me directly and indirectly:
- Leandra Bareiss: for being so patient with me.
- Florian Roth / Thomas Patzke: for developing the great tool Sigma
- Olaf Hartong: for his great Threat Hunting App, which inspired me
- Freddy Dezeure: for supporting me
- Andrii Bezverkhyi: for supporting with Splunk questions
- Chris Long: for Detection Lab
- SwiftOnSecrity: for the Sysmon Config, which I used in all of my tests
