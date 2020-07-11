<template>
  <div id="app">
	<ThePreface/>
	<div>
		<CourseCard 
			v-for="course in Object.keys(courseData).sort()"
			v-bind:key="courseData[course].courseTitleFull"
			v-bind:courseTitleFull="courseData[course].courseTitleFull"
			v-bind:courseDetails="courseData[course].courseDetails"
			v-bind:coursePrerequisites="courseData[course].coursePrerequisites"
			v-bind:tags="courseData[course].tags"
		/>
	</div>
  </div>
</template>

<script>
import ThePreface from './components/ThePreface.vue'
import CourseCard from './components/CourseCard.vue'
import courseData from './json/course-data.json'

export default {
	name: 'App',
	data(){
		return {
			courseData: courseData
		}
	},
	components: {
		ThePreface,
		CourseCard
	}
}
</script>

<style>
#app {
	font-family: Avenir, Helvetica, Arial, sans-serif;
	color: #243649;
}
</style>
