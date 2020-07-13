<template>
	<div class="preface">
		<h1>Course Checker</h1>

		<h2>What is this?</h2>
		<p>This tool displays and filters data scraped from the UTM timetable for the 2020-2021 fall/winter session (with the exception of a hard coded course that is only offered in the summer). It currently focuses on courses for the CCIT major, which excludes any course not beginning with CCT and any course that has a restriction to exclude CCIT majors.</p>		
			
		<h2>Why is this a thing?</h2>
		<p>Currently the official UTM timetable displays CCIT, DEM, and PWC program courses under on subject area due to them being offered by the same department. However, I am only interested in courses that a CCIT major can take. Having to scroll through courses I am restricted from taking or simply not for my program is annoying. For example, most course codes starting with MGD or include DEM in the title will not allow CCIT majors to enroll.</p>
	</div>
</template>

<script>
export default {
	name: 'ThePreface'
}
</script>

<style scoped>
.preface {
	margin: 1.5em;
}
</style>
