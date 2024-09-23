<script lang="ts">
  import { enhance } from "$app/forms";
  import type { ActionData } from "./$types";

  export let form: ActionData;
</script>

<svelte:head>
  <title>Register New User</title>
</svelte:head>

<div class="flex items-center justify-center min-h-screen bg-gray-100">
  <div
    class="w-full max-w-md p-8 bg-white rounded-lg shadow-lg border border-gray-200"
  >
    <h1 class="text-3xl font-bold mb-6 text-center">Create Your Account</h1>

    {#if form?.error}
      <div
        class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative mb-4"
        role="alert"
      >
        <span class="block sm:inline">
          {@html form?.message}
        </span>
      </div>
    {/if}

    <form method="POST" action="/register" class="space-y-6" use:enhance>
      <div>
        <label for="username" class="block text-lg font-medium text-gray-700"
          >Username</label
        >
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
        <label for="password" class="block text-lg font-medium text-gray-700"
          >Password</label
        >
        <div class="relative">
          <input
            type="password"
            id="password"
            name="password"
            required
            class="mt-1 block w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
            placeholder="Enter your password"
          />

          <div
            class="absolute top-1/2 right-3 transform -translate-y-1/2 group"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              xmlns:xlink="http://www.w3.org/1999/xlink"
              fill="#3775A9"
              version="1.1"
              width="16"
              height="16"
              viewBox="0 0 416.979 416.979"
              class="ml-2 text-gray-400 cursor-pointer"
              xml:space="preserve"
            >
              <g>
                <path
                  d="M356.004,61.156c-81.37-81.47-213.377-81.551-294.848-0.182c-81.47,81.371-81.552,213.379-0.181,294.85   c81.369,81.47,213.378,81.551,294.849,0.181C437.293,274.636,437.375,142.626,356.004,61.156z M237.6,340.786   c0,3.217-2.607,5.822-5.822,5.822h-46.576c-3.215,0-5.822-2.605-5.822-5.822V167.885c0-3.217,2.607-5.822,5.822-5.822h46.576   c3.215,0,5.822,2.604,5.822,5.822V340.786z M208.49,137.901c-18.618,0-33.766-15.146-33.766-33.765   c0-18.617,15.147-33.766,33.766-33.766c18.619,0,33.766,15.148,33.766,33.766C242.256,122.755,227.107,137.901,208.49,137.901z"
                />
              </g>
            </svg>
            <div
              class="absolute left-0 mt-2 w-64 p-3 bg-gray-200 border border-gray-400 rounded-lg shadow-lg hidden group-hover:block"
            >
              <p class="text-gray-600 text-sm">
                NOTE: Due to new security requirements we have revamped the
                password collision mechanism to prevent reuse.
              </p>
            </div>
          </div>
        </div>
      </div>

      <div class="flex justify-between items-center">
        <button
          type="submit"
          class="bg-blue-600 text-white py-2 px-6 rounded-lg hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
        >
          Register
        </button>

        <a href="/login" class="text-blue-600 hover:text-blue-800 font-medium">
          Login
        </a>
      </div>
    </form>
  </div>
</div>
