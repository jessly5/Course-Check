<template>
  <div id="app">
	<h1>Course Checker</h1>
	<div>
		<h2>What is this?</h2>
		<p>This tool displays and filters data scraped from the UTM timetable for the 2020-2021 fall/winter session. It currently focuses on CCIT courses, which excludes any course not beginning with CCT and any course that is restricted to DEM.</p>		
		<h2>Why is this a thing?</h2>
		<p>Currently the timetable displays all the ICCIT courses under one subject area. ICCIT currently hosts three programs, and they are all jumbled together in alphabetical order due to being under the same filter. It gets quite tiresome to scroll through courses I am restricted from taking or just simply not in my program. For example, most courses codes starting with MGD or include DEM in the title will not allow CCIT majors to enroll. In addition, PWC program courses are always listed at the bottom since they start with WRI. It just doesn't make sense, and is really annoying! I've emailed the UTM Registrar about my complaint, but I do not know if they will fix it.</p>
	</div>
	<div>
		<Course 
			v-for="data in course_data"
			v-bind:key="data.courseTitleFull"
			v-bind:courseTitleFull="data.courseTitleFull"
			v-bind:courseDetails="data.courseDetails"
			v-bind:coursePrerequisites="data.coursePrerequisites"
			v-bind:tags="data.tags"
		/>
	</div>
  </div>
</template>

<script>
import Course from './components/Course.vue'
import json from './json/course-data.json'

export default {
  name: 'App',
  data(){
	return {
		course_data: json
	}
  },
  components: {
	Course
  }
}
</script>

<style>
#app {
	font-family: Avenir, Helvetica, Arial, sans-serif;
}
</style>
