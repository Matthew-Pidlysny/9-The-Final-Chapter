/*
 * MainWindow.h - Main Application Window
 */

#ifndef MAIN_WINDOW_H
#define MAIN_WINDOW_H

class PlanePilotApp;

class MainWindow {
public:
    explicit MainWindow(PlanePilotApp* app);
    ~MainWindow();
    
    bool initialize();
    void update();
    void render();
    
    bool shouldExit() const { return m_shouldExit; }
    bool shouldGoToWorkshops() const { return m_shouldGoToWorkshops; }

private:
    PlanePilotApp* m_app;
    bool m_shouldExit;
    bool m_shouldGoToWorkshops;
};

#endif // MAIN_WINDOW_H