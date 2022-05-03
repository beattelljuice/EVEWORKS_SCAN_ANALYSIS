# EVEWORKS SCAN ANALYSIS
<h2>Usage</h2>
<h3>Usage - Overview</h3>
<p>The EVEWORKS SCAN ANALYSIS is intended to be used in conjunction with the videogame Eve Online (Property of CCP)<br></p>
<h3>Usage - End User</h3>
<p>The End User of this application when deployed is intended to directly paste <b>Directional Scanner</b> Information and <b>Local Chat Window Members</b> Information found within Eve Online</p>

# Deployment
<h2>First Time Installation</h2>
<h3>Dependancies</h3>
<p>Use the <code> install_requirements.sh</code> script to install all libraries that dont automatically come with python3.8</p>
<p>The Manual Process to install dependancies is</p>
<code>pip install pyYaml</code><br>
<code>pip install Cherrypy</code><br>
<code>pip install pyJWT</code>
<h3>Running the program</h3>
<p>Run the program via python <code>python3 main.py</code></p>
<h3>Config.json</h3>
<p><code><b>URI</b></code> : The hostname/ip address the server should listen on</p>
<p><code><b>DEBUG</b></code> : true/<b>false</b> : weither or not to print a bunch of extra debugging junk</p>
<p><code><b>USE ID WHITELIST UPDATER</b></code> : <b>true</b>/false : weither or not to activate the automatic ID whitelist updater - Used for ensuring Ship Group ID dictionaries stay up to date to any ingame changes</p>

<h3>Common Errors</h3>
<h4>Error</h4>
<code>FileNotFoundError: [Errno 2] No such file or directory: 'dscans/count.dat'</code>
<br>
<h4>Solution</h4>
<p>1. Ensure the <code>dscan/</code> directory exists</p>
<p>2. Inside the <code>dscan/</code> directory create a file <code>count.dat</code> and insert <code>0</code> into the file</p>
<p>3. Delete all the <code>.scan</code> files currently present<p>
