"""Dictator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from Dictator_service import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^users/', views.UserList.as_view()),
	url(r'^csrf/', views.SetCsrf.as_view()),
	url(r'^scan/', views.StartScan.as_view()),
	url(r'^switches/',views.Switches.as_view()),
	url(r'^project_status/', views.ProjectStatus.as_view()),
	url(r'^scan_concurrent/', views.StartScanConcurrent.as_view()),
	url(r'^polling/', views.PollingConfig.as_view()),
	url(r'^percentPolling/', views.PercentPolling.as_view()),
	url(r'^polling_scanning/', views.PollingExploit.as_view()),
	url(r'^scanning_st_up/', views.ScannningStUp.as_view()),
	url(r'^stop/', views.StopScan.as_view()),
	url(r'^stop_conc/', views.StopScanConc.as_view()),
	url(r'^stop_scanning/', views.StopExploits.as_view()),
	url(r'^resume/', views.ResumeScan.as_view()),
	url(r'^resume_conc/', views.ResumeScanConc.as_view()),
	url(r'^resume_scanning/', views.ResumeExploits.as_view()),
	url(r'^projects/', views.ExploitableProjects.as_view()),
	url(r'^config/', views.ExploitConfig.as_view()),
	url(r'^config_conc/', views.ExploitConfigConc.as_view()),
	url(r'^config_overwrite/', views.ExploitConfig_overwrite.as_view()),
	url(r'^launch_scanning/', views.LaunchExploits.as_view()),
	url(r'^launch_scanning_concurrent/',views.LaunchExploitsConcurrent.as_view()),
	url(r'^upload/', views.UploadNmapXml.as_view()),
	url(r'^uploadNessus/', views.UploadNessusXml.as_view()),
	url(r'^uploadQualys/', views.UploadQualysXml.as_view()),
	url(r'^mergeReports/', views.MergeReports.as_view()),
	url(r'^reportOnFly/', views.ReportOnFly.as_view()),
	url(r'^downloadAll/', views.DownloadAllMannual.as_view()),
	url(r'^Add/',views.AddTestCase.as_view()),
	url(r'^ScanProfiles/',views.ScanProfiles.as_view()),
	url(r'^ScanProfiles/',views.ScanProfiles.as_view()),
	url(r'^ScanProfile/',views.ScanProfile.as_view()),
	#url(r'^nessusOnFly/', views.NessusOnFly.as_view()),

	
]


