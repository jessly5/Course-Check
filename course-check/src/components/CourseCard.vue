<template>
  <div class="course">
    <h3>{{ courseTitleFull }}</h3>
	<hr>
	<p class="description"><strong>Description:</strong> {{ courseDetails }}</p>
	<p><strong>Prerequisites:</strong> {{ coursePrerequisites }}</p>
	<div class="flex-container"><strong>Tags:</strong>
		<span class="tag" v-for="t in tags" v-bind:key="t">{{ t }}
		</span>
	</div>
  </div>
</template>

<script>
export default {
	name: 'CourseCard',
	props: {
		courseTitleFull: String,
		courseDetails: String,
		coursePrerequisites: String,
		tags: Array
  }
}
</script>

<style scoped>
.course {
	text-align: left;
	border: 1.5px solid #243649;
	border-radius: 2em;
	padding: 2em;
	margin: 1.5em;
	background: #D9EBFF;
}
.tag {
	border: 1.5px solid #243649;
	border-radius: 2em;
	margin: 0.5em;
	padding: 0.5em;
	background: #F7F9F9;
}
.flex-container {
	display: flex;
	flex-flow: row wrap;
}
hr {
	border: none;
	background: #243649;
	height: 1.5px;
}
</style>
