install:
	if [ ! -d "/etc/hpctools" ]; then mkdir -p /etc/hpctools; fi
	cp config /etc/hpctools
	cp clustercp /usr/bin/
	cp clusterexec /usr/bin/

clean:
	rm -rf /etc/hpctools
	rm /usr/bin/clustercp
	rm /usr/bin/clusterexec 
