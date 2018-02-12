"""
This file is used in the cleanup script if the the boolean "use_external_grouping_file" is set to True.
If that variable is set to True, then the script will use the names of the lists/arrays in this file to sort all of the files by their extensions that are listed bellow. This file is fully customizable to your liking. 

The way that you can customize this file is as follows:
	Let's say that you want all the Microsoft Office files by them self and not included in the Documents list, then just remove the extensions from the list and make a new one. Make sure you use "ctrl" + "f" to find if those extensions arent in other parts of this file.

If for some reason a file extension is not listed (I'm not perfect), then the script will put all those files in one folder with the name of the extension.
		For example: if the extension iso is not listed (it is under Documents at the end), then the script would make a folder in the destination folder with the name "iso" and put all the iso's in that folder.


I obtained all the file extensions and organized them as they are bellow from this website:
	https://www.file-extensions.org/extensions/common-file-extension-list
"""


#######################################################################################################


""" 
If this variable is set to True then the script will make a folder with the name of the list and then inside that folder make a folder with the file extension of the file that is copied.

	Example: - Clean Folder    (Main folder)
				|- Documents   (Folder created from the name of the lists bellow inside the main folder.)
					|- accdb   (Folder inside the Documents folder containing all the files with this extension.)
					|- accdt        (These folders would only be created if there are files with this extension.)
					|- doc
					|- docm
					|......
				|- Audio
					|- 3ga
					|- aac
					|......

If the variable is set to False, then all the files with the extensions that are in the lists bellow will be copied into a folder with the name of the list.
"""
create_folder_of_extensions = False


"""
If set to True, then make sure that the "extensions_not_included" is present at the bottom. The list is, as of right now, at the bottom.
If set to False, then the script will copy all the files in the directory.
"""
do_not_include_list = True  # Usually I would leave this True if this file is used.


Extensions = {
	"Documents": {  # Make sure that this is the name of the folder that you want to contain the files with the extensions bellow.
	
		# Microsoft Office Files
		"accdb", "accdt", "doc", "docm", "docx", "dot", "dotm", "dotx", "mdb", "mpd", "mpp", "mpt", "oft", "one", "onepkg", "pot", "potx", "pps", "ppsx", "ppt", "pptm", "pptx", "pst", "pub", "snp", "thmx", "vsd", "vsdx", "xls", "xlsm", "xlsx",
		
		# E-book Files
		"azw", "azw3", "azw4", "cbr", "cbz", "epub", "fb2", "iba", "ibooks", "lit", "mobi",
		
		# Font Files
		"eot", "otf", "ttc", "ttf", "woff",
		
		# Simple Text Files
		"1st", "alx", "application", "asp", "csv", "eng", "log", "lrc", "nfo", "opml", "plist", "reg", "rep", "rtf", "srt", "sub", "tbl", "text", "txt", "xml", "xsd", "xsl", "xslt",
		
		# Internet Related Files
		"ashx", "asp", "aspx", "atom", "bc", "bc!", "class", "crdownload", "css", "dic", "download", "eml", "flv", "gdoc", "gsheet", "gslide", "htm", "html", "js", "json", "jsp", "jws", "mht", "opml", "part", "partial", "php", "png", "rss", "swf", "torrent", "webm", "webp", "xap", "xml", "xsd", "xsl", "xslt", 
		
		# Email Files
		"dbx", "eml", "ldif", "mht", "msg", "pst", "vcf",
		
		# Random list of document files (no order)
		"1st", "abw", "alx", "application", "asp", "aww", "chm", "cnt", "csv", "dbx", "djvu", "doc", "docm", "docx", "dot", "dotm", "dotx", "eng", "epub", "gp4", "htm", "html", "ind", "indd", "key", "keynote", "log", "lrc", "lst", "mht", "mpp", "nfo", "odf", "ods", "odt", "opml", "ott", "oxps", "pages", "pdf", "plist", "pmd", "pot", "potx", "pps", "ppsx", "ppt", "pptm", "pptx", "prn", "prproj", "ps", "pub", "pwi", "reg", "rep", "rtf", "sdd", "sdw", "shs", "snp", "srt", "sub", "sxw", "tbl", "text", "txt", "tpl" "vsd", "wpd", "wps", "wri", "xls", "xlsm", "xlsx", "xml", "xmp", "xps", "xsd", "xsl", "xslt",
		
		# ISOs
		"iso"
	},
	
	"Audio": {  # Make sure that this is the name of the folder that you want to contain the files with the extensions bellow.
		
		"3ga", "aac", "aiff", "amr", "ape", "arf", "asf", "asx", "cda", "dvf", "flac", "gp4", "gp5", "gpx", "logic", "m4a", "m4b", "m4p", "midi", "mp3", "ogg", "pcm", "rec", "snd", "sng", "uax", "wav", "wma", "wpl", "zab"
	},
	
	"Images": {  # Make sure that this is the name of the folder that you want to contain the files with the extensions bellow.
	
		# Bitmap Images
		"bmp", "cpt", "dds", "dib", "dng", "dt2", "emf", "gif", "ico", "icon", "jpeg", "jpg", "pcx", "pic", "png", "psd", "psdx", "tga", "thm", "tif", "tiff", "wbmp", "wdp", "webp",
		
		# Raw Images
		"arw", "cr2", "crw", "dcr", "dng", "fpx", "mrw", "nef", "orf", "pcb", "ptx", "raf", "raw", "rw2",
		
		# Vector Graphics
		"ai", "cdr", "csh", "csl", "drw", "emz", "odg", "pic", "sda", "svg", "svgz", "swf", "wmf",
		
		# Graphics File Types
		"abr", "ai", "ani", "cdt", "djvu", "eps", "fla", "icns", "ico", "icon", "mdi", "odg", "pic", "prn", "psb", "psd", "pzi", "sup", "vsdx", "xmp",
		
		# 3d Graphics
		"3d", "3ds", "c4d", "dgn", "dwfx", "dwg", "dxf", "ipt", "icf", "max", "pro", "skp", "stl", "u3d", "x_t",
		
		# GIFs
		"gif",
	},
	
	"Videos": { # Make sure that this is the name of the folder that you want to contain the files with the extensions bellow.
	
		"264", "3g2", "3gp", "arf", "asf", "asx", "avi", "bik", "dash", "dat", "dvr", "flv", "h264", "m2t", "m2ts", "m4v", "mkv", "mod", "mov", "mp4", "mpeg", "mpg", "mts", "ogv", "rec", "rmvb", "swf", "tod", "tp", "ts", "vob", "webm", "wimp" ,"wmv"
	},
	
	"Compressed_Files": {  # Make sure that this is the name of the folder that you want to contain the files with the extensions bellow.
	
		"7z", "arj", "cab", "cso", "deb", "gz", "gzip", "hqx", "isz", "rar", "rpm", "sis", "sisx", "sit", "sitd", "sitx", "tar", "tar.gz", "tgz", "zip"
	}
}


#######################################################################################################


number_of_extensions_in_list = len(Extensions)


""" Should only include the extensions that you don't want to copy over. """
extensions_not_included = ["ini", "lnk"]
