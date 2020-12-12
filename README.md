# Image-Download-Tools

This is the set of tools I use to download and manage downloaded pictures. I had tried several different ones, but none did things in a way that worked for me.

Many of my image searches are related to researching a topic or watching for new pictures related to a topic of interest. To accomplish that, I have built two programs that have Guru Prasad Singh's Bing Image Downloader at their heart.


## getimgs.py

This program gets images based on search terms, stores them in the __Images__ directory (with a name that includes the search term and a timestamp), and then deletes any duplicate files in the __Images__ directory.

An example of where this is useful is that if I did a search for `Cromemco S100 Systems` ever month or two, the resulting directory would only have pictures that I had not seen before once the run was complete. This lets you effectively build a 'baseline' of images related to a topic, and then add what is new to that over time.


## getset.py

This program gets images based on search terms and stores them in the __ImageSets__ directory (with a name that includes the search term and a timestamp). It does delete duplicate files within the subdirectory itself, but does not delete duplicate files across subdirectorys. Sometimes this doesn't matter, but at other times where there are limited search results Bing will return links to the same image multiple times and this will better handle those situations (although if the files have the same name, they overwrite themselves anyway).

An example of where this is useful is if I'm writing a blog that talks about vintage transistor radios, I might want to search for `GE vintage transistor radio` and for `vintage tabletop transistor radio`. In these cases, I would rather a duplicate picture be kept so that I don't have to search through multiple subdirectories that if I did a search for 'Cromemco S100 Systems' ever month or two, the resulting directory would only have pictures that I had not seen before once the run was complete. This lets you effectively build a 'baseline' of images related to a topic, and then add what is new to that over time.

