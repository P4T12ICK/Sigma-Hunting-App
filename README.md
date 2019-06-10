# Sigma-Hunting-App
A Splunk App containing Sigma detection rules, which can be updated dynamically from a Git repository.

## Motivation
Most of the modern Security Operations Center (SOC) store the detection rules in a central repository such as GitHub or GitLab as part of the Dev Sec Ops development approach. Furthermore, [Sigma](https://github.com/Neo23x0/sigma) as a generic signature description language is used in many SOCs. Updating the Sigma rules from a Sigma repository to Splunk was still a manual time-consuming task. The Sigma Hunting App solves that problem by providing a dedicated Splunk App, which can be used to dynamically update Sigma detection rules from a Git repository. The triggered detection rules are stored in a separate threat-hunting index helping the SOC Analyst in their investigations. Additionally, the Sigma Hunting App for Splunk uses information of the [Mitre ATT&CK Matrix](https://attack.mitre.org/matrices/enterprise/) to enrich the triggered detection rules. 

The Sigma Hunting App for Splunk provides the following features:
- dynamically update of Sigma detection rules from a remote Git repository
- Store triggered detection rules in a dedicated index
- Enrichment of triggered detection rules with data from the [Mitre ATT&CK Matrix](https://attack.mitre.org/matrices/enterprise/)
- Providing powerfull dashboards for investigation: security posture, host investigator, APT investigator, lateral movement investigator
- Whitelist App to adapt the detection rules to your enviroment

### Update of Sigma Detection Rules


### Store triggered Detection Rules in a dedicated Index


### Enrichment with Mitre ATT&CK Data


### Providing Investigation Dashbaords


### Splunk Sigma Hunting Whitelist App



