<script lang="ts">
	import { enhance } from "$app/forms";
	import type { ActionData } from "./$types";

	export let form: ActionData;
</script>

<svelte:head>
	<title>Login</title>
</svelte:head>

<div class="flex items-center justify-center min-h-screen bg-gray-100">
  <div class="w-full max-w-md p-8 bg-white rounded-lg shadow-lg border border-gray-200">
    <h1 class="text-3xl font-bold mb-6 text-center">Login to Your Account</h1>

    {#if form?.error}
      <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative mb-4" role="alert">
        <span class="block sm:inline">
          {@html form?.message}
        </span>
      </div>
    {/if}

    <form method="POST" action="/login" class="space-y-6" use:enhance>
      <div>
        <label for="username" class="block text-lg font-medium text-gray-700">Username</label>
        <input 
          type="text" 
          id="username" 
          name="username" 
          required 
          class="mt-1 block w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
          placeholder="Enter your username"
        />
      </div>

      <div>
        <label for="password" class="block text-lg font-medium text-gray-700">Password</label>
        <input 
          type="password" 
          id="password" 
          name="password" 
          required 
          class="mt-1 block w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
          placeholder="Enter your password"
        />
      </div>

      <div class="flex justify-between items-center">
        <button 
          type="submit" 
          class="bg-blue-600 text-white py-2 px-6 rounded-lg hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
        >
          Login
        </button>

        <a 
          href="/register" 
          class="text-blue-600 hover:text-blue-800 font-medium"
        >
          Register
        </a>
      </div>
    </form>
  </div>
</div>