function toggleNav() {
	if (document.getElementById("side_bar").offsetWidth>0) {
		document.getElementById("side_bar").style.width="0%";
		document.getElementById("content").style.marginLeft="0%";
	}
	else {		
		document.getElementById("side_bar").style.width = "14%";
		document.getElementById("content").style.marginLeft = "14%";
	}
}