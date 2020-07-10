<template>
  <div id="app">
	<ThePreface/>
	<div>
		<CourseCard 
			v-for="data in courseData"
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
