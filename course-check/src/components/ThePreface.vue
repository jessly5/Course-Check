<template>
  <div class="preface">
	<h1>Course Checker</h1>

	<h2>What is this?</h2>
	<p>This tool displays and filters data scraped from the UTM timetable for the 2020-2021 fall/winter session. It currently focuses on CCIT courses, which excludes any course not beginning with CCT and any course that is restricted to DEM.</p>		
		
	<h2>Why is this a thing?</h2>
	<p>Currently the timetable displays all the ICCIT courses under one subject area, even though ICCIT currently hosts three programs. The courses are all together in alphabetical order due to being under the same subject area filter. It's annoying scrolling through courses I am restricted from taking or just simply not in my program. For example, most courses codes starting with MGD or include DEM in the title will not allow CCIT majors to enroll. In addition, PWC program courses are always listed at the bottom since they start with WRI. I've emailed the UTM Registrar about my complaint, but I do not know if they will fix it.</p>
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
