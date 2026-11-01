package com.zendooh

import androidx.compose.ui.test.assertIsDisplayed
import androidx.compose.ui.test.junit4.createComposeRule
import androidx.compose.ui.test.onNodeWithText
import org.junit.Rule
import org.junit.Test

class AppTest {
    @get:Rule
    val compose = createComposeRule()

    @Test
    fun displaysApplicationName() {
        compose.setContent { App() }
        compose.onNodeWithText("Zendooh").assertIsDisplayed()
    }
}
